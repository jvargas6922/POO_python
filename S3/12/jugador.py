# Description: Clase Jugador que hereda de Personaje y tiene un atributo arma
import random
from personaje import Personaje

class Jugador(Personaje):
    # Constructor
    # Se inicializa con los atributos de un personaje y un arma
    def __init__(self, hp: int, atk: int, df: int, arma: str = None) -> None:
        #con super() se llama al constructor de la clase padre
        super().__init__(hp, atk, df)
        self.__arma = arma

    #Métodos getter y setter
    def ataque(self) -> int:
        return (self.atk + random.randint(1, 5)
            if self.arma else self.atk)
    
    #polimorfismo en el metodo setter
    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - random.randint(1, self.df), 0)