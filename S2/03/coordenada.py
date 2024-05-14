"""
METODO OTHER
"""
class Coordenada():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #     nuevo_x = self.x + other.x
    #     nuevo_y = self.y + other.y
    #     return Coordenada(nuevo_x, nuevo_y)

    def __eq__(self, other):
        compara_x = self.x == other.x
        compara_y = self.y == other.y
        return compara_x and compara_y
    
