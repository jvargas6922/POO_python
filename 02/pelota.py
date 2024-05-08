class Pelota():
    forma = "redonda"
    material = "cuero"
    color = "blanco"
    diametro = 22

#METODOS ESTÁTICO
    @staticmethod
    def rodar():
        print("La pelota está rodando")

    @staticmethod
    def rebotar():
        print("La pelota está rebotando")

    @staticmethod
    def girar():
        print("La pelota está girando")
    
    @staticmethod
    def crear_rebote():
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
    
    #METODO NO ESTATICOS
    #METODO PARA CAMBIAR COLOR
    def asignar_color(self, nuevo_color: str):
        self.color = nuevo_color

    #METODO DE INSTANCIA QUE LEE EL COLOR DE LA INSTANCIA
    def leer_color(self):
        print("El color de esta pelota es {}".format(self.color))

    def lee_color_local_y_atributo(self, color_local: str):
        # Esta variable "color" sólo existe en el alcance del método
        color = color_local
        self.leer_color()
        print("El color {} NO es el color de ESTA pelota".format(color))
    