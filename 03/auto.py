class Auto():
    marca = "Ford"
    modelo = "Fiesta"
    color = "Rojo"
    puertas = 4
    motor = 1.6

#METODOS ESTÁTICO
@staticmethod
def encender():
    print("El auto está encendido")

@staticmethod
def apagar():
    print("El auto está apagado")

@staticmethod
def acelerar():
    print("El auto está acelerando")

@staticmethod
def frenar():
    print("El auto está frenando")

#METODOS NO ESTÁTICOS
def __init__(self):
    print("Se ha creado un auto")

