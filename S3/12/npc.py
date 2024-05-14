class NPC():
    def __init__(self, nombre: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__nombre = nombre

    def mostrar_dialogo(self, mensaje: str) -> None:
        print(f"{self.__nombre}: {mensaje}")