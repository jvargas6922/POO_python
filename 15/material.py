class Material():
    def __init__(self, nombre:str, duracion:str, textura:str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota():
    def __init__(self, tamanio:int, color:str, material: Material):
        self.tamanio = tamanio
        self.color = color
        # La pelota tiene un material
        self.material = material