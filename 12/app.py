from abc import ABC, abstractmethod
class Pelota(ABC):
    @abstractmethod
    def rebotar(self, altura: int):
        pass

class PelotaDeJuguete(Pelota):
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, nuevo_color: str):
        # Puede modificar el atributo privado, porque está dentro de la clase
        self.__color = nuevo_color

    def rebotar(self, altura: float):
        pass

p = PelotaDeJuguete("amarilla")
# print(p.__color)
print(p.color)