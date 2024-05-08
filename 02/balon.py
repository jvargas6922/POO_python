class Balon():
    forma = "redonda"

    def asignar_color(self, nuevo_color: str):
        self.color = nuevo_color

    def lee_color_y_forma(self):
        print(f"El color de esta pelota es {self.color}")
        print(f"La forma de esta pelota es {self.forma}")