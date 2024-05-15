# Description: Clase abstracta Personaje
from abc import ABC, abstractmethod
# Clase abstracta Personaje
class Personaje(ABC):
    # Constructor
    # Se inicializa con los atributos de un personaje
    #kwargs: diccionario de atributos
    #hp: vida
    #atk: ataque
    #df: defensa
    #atributos privados
    def __init__(self, hp: int, atk: int, df: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__hp = hp
        self.__atk = atk
        self.__df = df

    #Métodos getter y setter
    @property
    def hp(self) -> int:
        return self.__hp
    
    @hp.setter
    def hp(self, hp) -> None:
        self.__hp = hp

    @property
    def atk(self) -> int:
        return self.__atk
    
    @property
    def df(self) -> int:
        return self.__df
    
    #Métodos abstractos
    #Método para atacar
    @abstractmethod
    def ataque(self) -> None:
        pass
    
    #Método para defenderse
    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass