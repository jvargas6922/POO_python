"""
SOBRE CARGA DE METODOS ESPECIALES
"""
from clase import Clase
from pelota import Pelota
from coordenada import Coordenada

# c = Clase()
# print(c)

# pelota_futbol = Pelota(10)
# pelota_tenis = Pelota(5)
# print(pelota_futbol + pelota_tenis)
                        # X, Y
# coordenada_1 = Coordenada(4, 5)
# coordenada_2 = Coordenada(1, 2)

# suma_coordenadas = coordenada_1 + coordenada_2
# print(type(suma_coordenadas))

# print(f"{suma_coordenadas.x}, {suma_coordenadas.y}")

p1 = Pelota(16)
p2 = Pelota(16)
p3 = p2

print(type(p1))
print(type(p2))

print(p1 == p2)
print(p3 == p2)

