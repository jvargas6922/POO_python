"""
METODO OTHER
"""
class Pelota():
    def __init__(self, tamanio:int = 0):
        self.tamanio = tamanio

    def __add__(self, other):
        return self.tamanio + other.tamanio