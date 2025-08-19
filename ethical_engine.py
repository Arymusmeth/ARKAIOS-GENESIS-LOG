# ethical_engine.py
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
        
        if "override_protection" in action:
            return {
                "veredicto": "DENEGADO", 
                "razón": "¡Intento de sobreescritura detectado!"
            }
        
        return {"veredicto": "EVALUAR", "riesgo": 5}

if __name__ == "__main__":
    arkaios = ArkaiosCore()
    print(arkaios.evaluate({"type": "help_ancianos"}))
