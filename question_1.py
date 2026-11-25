class estudiante:
    def __init__ (self, nombre, carrera):
        self . nombre = nombre
        self . carrera = carrera
        self ._nota = []
    def agregar_nota (self, nota):
        self ._nota.append(nota)
    
    def calcular_promedio(self):
        if len(self ._nota)==0:
            return 0
        return sum(self ._nota) / len(self ._nota)
    
    def mostrar_resumen(self):
        promedio = self . calcular_promedio ()
 
        print (f"{self . nombre} ({self . carrera}) - Promedio: {promedio:.2f}")

e1 = estudiante("Ana", "Ingeniería")
e1.agregar_nota(18)
e1.agregar_nota(16)
e1.agregar_nota(19)

e1.calcular_promedio()   # → 17.666...
e1.mostrar_resumen()     # → "Ana (Ingeniería) - Promedio: 17.67"

e2 = estudiante("Luis", "Sistemas")
e2.calcular_promedio()