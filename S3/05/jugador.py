import random
from personaje import Personaje

#Clase Jugador
class Jugador(Personaje):
    
    def ataque(self) -> int:
        return (self.atk + random.randint(1, 5) if self.arma else self.atk)
    
    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - random.randint(1, self.df), 0)