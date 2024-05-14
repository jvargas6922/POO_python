from abc import ABC, abstractmethod

class PelotaAbstracta(ABC):
    @abstractmethod
    def rebotar(self, altura:int):
        pass

class PelotaDeJuguete(PelotaAbstracta):
    def rebotar(self, altura:float):
        self.rebotes =[]
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura //= 2


pelota = PelotaDeJuguete()
pelota.rebotar(100)
print(pelota.rebotes)