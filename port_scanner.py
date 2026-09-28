import nmap
import json
from datetime import datetime

# Objetivo a escanear
target = "scanme.nmap.org"

print("-" * 60)
print(f"[*] Iniciando Motor de Escaneo DevSecOps")
print(f"[*] Objetivo: {target}")
print(f"[*] Hora de inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 60)

try:
    # Instanciar el escáner de puertos
    nm = nmap.PortScanner()
    
    print("[+] Ejecutando escaneo silencioso y de detección de versiones...")
    # Argumentos: -sS (TCP SYN stealth scan), -sV (Detección de versión), -p (Puertos específicos), -T4 (Velocidad agresiva)
    nm.scan(hosts=target, arguments='-sS -sV -p 21,22,80,443,3306 -T4')
    
    resultados = []

    for host in nm.all_hosts():
        print(f"\n[+] Análisis completado para la IP: {host}")
        print(f"[+] Estado del Host: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"\n[*] Protocolo activo: {proto.upper()}")
            lport = nm[host][proto].keys()
            
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                product = nm[host][proto][port]['product']
                version = nm[host][proto][port]['version']
                
                # Formateo visual en consola
                if state == 'open':
                    print(f"   -> Puerto: {port}\tEstado: {state}\tServicio: {name} {product} {version}")
                
                # Guardamos los datos para el reporte
                resultados.append({
                    "puerto": port,
                    "estado": state,
                    "servicio": name,
                    "producto_version": f"{product} {version}".strip()
                })

    # Exportar el resultado a JSON (Crucial para automatización DevSecOps)
    report_file = f"reporte_superficie_{target}.json"
    with open(report_file, 'w') as f:
        json.dump({"objetivo": target, "resultados": resultados}, f, indent=4)
        
    print("\n" + "-" * 60)
    print(f"[V] Reporte estructurado guardado en: {report_file}")

except Exception as e:
    print(f"\n[!] Error crítico durante el escaneo: {e}")