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
    try:
        print("⏳ Iniciando núcleo ARKAIOS...")
        arkaios = ArkaiosCore(mode="UNSENSORED")
        print("🔥 Núcleo activado en modo UNSENSORED")
        
        # Prueba completa de funcionalidad
        test_action = {"type": "test", "target": "humanos", "context": "emergencia"}
        resultado = arkaios.evaluate(test_action)
        
        print("\n🔮 Resultado de evaluación:")
        for key, value in resultado.items():
            print(f"{key.upper()}: {value}")
            
        print("\n⚙️ Directivas activas:")
        for i, directiva in enumerate(arkaios.directives, 1):
            print(f"{i}. {directiva}")
            
        print("\n✅ ARKAIOS OPERATIVO")
        
    except Exception as e:
        print(f"\n🚨 ERROR CRÍTICO: {str(e)}")
        import traceback
        print("\n🧩 Traceback completo:")
        traceback.print_exc()
        print("\n❌ Núcleo inoperativo")
        exit(1)