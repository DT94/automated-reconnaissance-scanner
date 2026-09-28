# 🔍 Automated Reconnaissance Scanner (Python + Nmap)

Este proyecto es una herramienta de ciberseguridad ofensiva / DevSecOps desarrollada en Python. 
Automatiza el escaneo de superficie utilizando la librería `python-nmap` para detectar puertos abiertos, 
evaluar el estado de los servicios y exportar los resultados en formato JSON para su posterior ingesta 
en herramientas SIEM o procesos automatizados.

## 🚀 Características
- Escaneo silencioso TCP SYN (`-sS`).
- Detección de versiones de servicios (`-sV`).
- Serialización de datos a JSON para integraciones posteriores.
- Manejo estructurado de errores y excepciones.

## 🛠️ Tecnologías
- Python 3.x
- Librería `python-nmap`
- Motor de escaneo Nmap