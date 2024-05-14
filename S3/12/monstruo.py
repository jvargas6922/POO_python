from personaje import Personaje
from npc import NPC

class Monstruo(Personaje, NPC):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)

    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - (self.df + int(self.hp*0.001)), 0)