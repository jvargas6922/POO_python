from personaje import Personaje
#Uso del Polimorfismo en Python
#Los métodos ataque y defensa son diferentes en cada clase
#Clase Monstruo
class Monstruo(Personaje):
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)
    
    def defensa(self, ataque: int) -> None:
        self.hp -= max(ataque - (self.df + int(self.hp*0.001)), 0)