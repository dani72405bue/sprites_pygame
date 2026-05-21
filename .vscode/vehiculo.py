# definicion de la clase del vehiculo 
class Vehiculo:
    # Constructor de la clase Veniculo
    def __init__(self, matricula, color, numeroPuertas):
        self.MATRICULA = matricula
        self. COLOR = color
        self. NUMERO = numeroPuertas
        self.AVANZA = False
        print ("Constucción de un vehículo : " + self. MATRICULA)

    # Metodo Avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + " avanza. ")
    # Metodo Detenerse
    def Detenerse(self):
        self. AVANZA = False
        print (self. MATRICULA + " se detiene.")
# Construcción de una primera instancia
vehiculol = Vehiculo("AR123", "rojo", 3)
# Construccion de una segunda instancia
vehiculo2 = Vehiculo("FR456", "verde", 5)
# EL priner vehiculo avanza
vehiculol.Avanzar()

# El primer vehículo se detiene
vehiculol.Detenerse()
