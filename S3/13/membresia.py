from abc import ABC, abstractmethod
#paso 1(CREAR LA CLASE MENBRESIA QUE ES UNA CLASE ABSTRACTA)
"""
RAZONAMIENTO:
    SE REALIZA EL CONTRUCTOR DE LA CLASE DONDE LE PASAMOS LOS PARAMETROS NECESARIOS PARA QUE LA CLASE SE PUEDA CREAR.
    SE CREA UNA CLASE ABSTRACTA QUE SE LLAMA MENBRESIA QUE HEREDA DE ABC
    SE CREA EL CONSTRUCTOR DE LA CLASE QUE RECIBE 2 PARAMETROS QUE SON EL CORREO DEL SUSCRIPTOR Y EL NUMERO DE TARJETA
    SE CREAN LOS GETTER PARA PODER OBTENER LOS VALORES DE LOS ATRIBUTOS
    SE CREA EL METODO ABSTRACTO QUE SE LLAMA CAMBIAR_SUSCRIPCION QUE RECIBE UN PARAMETRO QUE ES EL TIPO DE MEMBRESIA
"""
#QUE RECIBE 2 PARAMETROS POR QUE CADA SUSCRIPCION POSEE CORREO_SUSCRIPTOR Y NUMERO DE TARJETA)
from abc import ABC, abstractmethod

# Clase abstracta Membresia
class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:  # Básica
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:  # Familiar
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:  # Sin Conexión
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:  # Pro
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

# Clase Gratis
class Gratis(Membresia):
    costo = 0
    dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Clase Basica
class Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)

        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7
        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Clase Familiar
class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        pass

# Clase SinConexion
class SinConexion(Basica):
    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        pass

# Clase Pro
class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


        



