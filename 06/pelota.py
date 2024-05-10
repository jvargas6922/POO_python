"""
CONSTRUCTORES
"""
class Pelota():
    # def __init__(self):
    #     print("Se ha creado una pelota")

    #ASIGNAR VALORES EN EL CUERPO DEL METODO
    # def __init__(self):
    #     self.color = "Rojo"
    #     self.tamanio = "Grande"
    #     self.material = "Plástico"

    #ASIGNAR VALORES DESDE LOS PARAMETROS DEL METODOS
    # def __init__(self, color:str, tamanio:int, material:str):
    #     self.color = color
    #     self.tamanio = tamanio
    #     self.material = material
    
    #ASIGNAR VALORES DESDE LOS PARAMETROS DEL METODO POR DEFECTO
    # def __init__(self, color="rojo", tamanio=10, material="Plástico"):
    #     self.color = color
    #     self.tamanio = tamanio
    #     self.material = material

    #USO DE ACCESADOR(GETTER) Y MODIFICADOR(SETTER)
    def __init__(self):
        self.color = "Blanco"
        self.material = "Plástico"
        self.tamanio_pelota = 2 

    @property
    def color_y_material(self):
        return f"Color: {self.color}, Material: {self.material}"
    
    @property
    def tamanio(self):
        return self.tamanio_pelota
    
    @tamanio.setter
    def tamanio(self, tamanio):
        # print(tamanio)
        # self.tamanio_pelota = tamanio if tamanio > 0 else 1
        #VALIDACION PARA QUE SOLO ME MUESTRE SI EL VALOR ES MAYOR A 0
        if tamanio < 0:
            self.tamanio_pelota = 1
        else:
            self.tamanio_pelota = tamanio