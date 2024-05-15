from personaje import Personaje
from npc import NPC

class Monstruo(Personaje, NPC):
    # Constructor
    #kwargs: diccionario de atributos
    def __init__(self, **kwargs) -> None:
        #con super() se llama al constructor de la clase padre
        super().__init__(**kwargs)
    
    #Método para atacar
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)

    #Método para defenderse
    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - (self.df + int(self.hp*0.001)), 0)