# Instalacion

instalar ambiente py con setup_xxx
Consigna.pdf

Informe en Informe folder

explicar gitignore.


metodos aplicado en Obligatorio_ML. explicar otras coasas


ver cofig + py interpreter con 


```python
import platform
import os
import sys
import json

try:
    import psutil
except ImportError:
    psutil = None


def get_system_info():
    info = {
        "os": {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "platform": platform.platform(),
        },
        "python": {
            "version": sys.version,
            "executable": sys.executable,
        },
        "environment_variables": dict(os.environ),
    }

    if psutil:
        info["hardware"] = {
            "cpu_count": psutil.cpu_count(logical=False),
            "cpu_count_logical": psutil.cpu_count(logical=True),
            "total_ram_bytes": psutil.virtual_memory().total,
            "disk_usage_root": {
                "total": psutil.disk_usage("/").total,
                "used": psutil.disk_usage("/").used,
                "free": psutil.disk_usage("/").free,
            },
        }
    else:
        info["hardware"] = "psutil no instalado"

    return info

if __name__ == "__main__":
    system_info = get_system_info()

    # Convertir a JSON (con pretty-print)
    json_output = json.dumps(system_info, indent=4, ensure_ascii=False)

    # Guardar en archivo
    with open("system_info.json", "w", encoding="utf-8") as f:
        f.write(json_output)

    print("Información del sistema guardada en system_info.json")
    print("\nVista previa:")
    print(json_output)
```