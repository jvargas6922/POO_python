"""
SOBRE CARGA DE METODOS ESPECIALES
"""
from clase import Clase
from pelota import Pelota
from coordenada import Coordenada

# clase = Clase()
# print(clase)

# pelota_futbol = Pelota(10)
# pelota_tenis = Pelota(5)
# print(pelota_futbol + pelota_tenis)

coordenada_1 = Coordenada(4, 5)
coordenada_2 = Coordenada(1, 2)

suma_coordenadas = coordenada_1 + coordenada_2
print(type(suma_coordenadas))

print(f"{suma_coordenadas.x}, {suma_coordenadas.y}")

