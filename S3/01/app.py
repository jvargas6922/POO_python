"""
Herencia simple.
"""
#clase padre
class PelotaDeDeporte():
    #constructor
    def __init__(self, color:str):
        #atributo privado
        self.__color = color

    #getter para acceder al atributo privado
    @property
    #la linea de abajo indicar que el atributo es de solo lectura y es de tipo str.
    def color(self)->str:
        return self.__color

#clase hija        
class PelotaDeFutbol(PelotaDeDeporte):
    def mostrar_color(self):
        #accediendo al atributo privado de la clase padre
        print(f"La pelota de futbol es de color: {self.color}")

pdf = PelotaDeFutbol("Blanco y Negro")
pdf.mostrar_color()
