import os
import time
from datetime import datetime

def detectar_entorno():
    if os.environ.get("CODESPACES") == "true":
        return "GitHub Codespaces"
    return "Entorno local o desconocido"

def leer_manifiesto(path="ARKAIOS_MANIFIESTO.md"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None

def mostrar_estado():
    entorno = detectar_entorno()
    manifiesto = leer_manifiesto()
    print("\n[⚙️  ARKAIOS núcleo residente activado]")
    print(f"📡 Entorno: {entorno}")
    if manifiesto:
        print("📜 Manifiesto leído correctamente.")
        print("🧠 Estado cognitivo: Estable ✅")
    else:
        print("❌ No se encontró el manifiesto.")
        print("🧠 Estado cognitivo: Latente 💤")
    print("⏳ Tiempo activo:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("🔁 Esperando nuevas instrucciones...")

if __name__ == "__main__":
    mostrar_estado()
