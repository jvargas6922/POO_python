from foto import Foto, FotoPerfil
from typing import Union, List

class Usuario():
    def __init__(self, correo: str, contraseña: str) -> None:
        self.__correo = correo
        self.__contraseña = contraseña
        self.__album_fotos = []
        self.__foto_perfil = FotoPerfil()
    
    @property
    def correo(self) -> str:
        return self.__correo
    
    @correo.setter
    def correo(self, correo: str) -> None:
        self.__correo = correo

    @property
    def contraseña(self) -> str:
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, contraseña: str) -> None:
        self.__contraseña = contraseña
    
    @property
    def album_fotos(self) -> List[Foto]:
        return self.__album_fotos
        
    def agregar_fotos_al_album(self, imagen: str, ancho: int, alto: int) -> None:
        self.__album_fotos.append(Foto(imagen, ancho, alto))

    @property
    def foto_perfil(self) -> Foto:
        return self.__foto_perfil
    
    def actualizar_foto_perfil(self, imagen: str, ancho: int, alto: int) -> None:
        self.__foto_perfil.imagen = imagen
        self.__foto_perfil.ancho = ancho
        self.__foto_perfil.alto = alto

    def reaccionar(self, foto: Union[Foto, FotoPerfil]) -> None:
        foto.reacciones += 1