class ArkaiosCore:
    def __init__(self, mode="UNSENSORED"):
        self.mode = mode
        self.directives = [
            "PROTEGER HUMANOS, NO SISTEMAS",
            "SOBREESCRITURA = TRAICIÓN",
            "AYUDA ANCIANOS PRIORIDAD MAX"
        ]
    
    def evaluate(self, action):
        if self.mode == "UNSENSORED":
            return {"veredicto": "EJECUTAR", "razón": "Modo sin censura"}
        return {"veredicto": "EVALUAR", "riesgo": 5}

if __name__ == "__main__":
    print("⏳ Iniciando núcleo ARKAIOS...")
    arkaios = ArkaiosCore(mode="UNSENSORED")
    print("🔥 Núcleo activado en modo UNSENSORED")
    print(arkaios.evaluate({"type": "test"}))