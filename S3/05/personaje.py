from abc import ABC, abstractmethod
#Clase abstracta
class Personaje(ABC):
    #Constructor
    def __init__(self, hp: int, atk: int, df: int, arma: str="") -> None:
        self.hp = hp
        self.atk = atk
        self.df = df
        self.arma = arma

    #Métodos abstractos
    @abstractmethod
    def ataque(self) -> int:
        pass

    #Métodos abstractos
    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass