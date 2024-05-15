class NPC():
    # Constructor
    # Se inicializa con un nombre y un diccionario de atributos
    def __init__(self, nombre: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__nombre = nombre

    #Método para mostrar un mensaje en consola
    def mostrar_dialogo(self, mensaje: str) -> None:
        print(f"{self.__nombre}: {mensaje}")