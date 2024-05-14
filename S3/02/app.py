"""
Herencia multiple en Python
Es cuando la clase hija hereda de dos o más clases padres
"""
#clase padre
class PelotaDeDeporte():

    tipo = "Deporte"
#clase padre
class PelotaDePlastico():
    tipo = "Plastico"

#clase hija
class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    pass

print(PelotaDePingPong.tipo)