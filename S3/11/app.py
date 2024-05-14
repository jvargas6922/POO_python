class PelotaDeDeporte():
    def __init__(self, color: str) -> None:

        if isinstance(self, PelotaDeTenis):
            self.__color = "Amarillo"
        else:
            self.__color = color
    @property
    def color(self) -> str:
        return self.__color
    
class PelotaDeTenis(PelotaDeDeporte):
    pass

p = PelotaDeTenis("Rojo")
# Salida: Amarillo
print(p.color)