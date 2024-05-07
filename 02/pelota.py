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