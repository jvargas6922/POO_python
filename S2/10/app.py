"""
Agregacion en Python
"""
from material import Material, Pelota
# from material import Pelota

m = Material("Plastico", "corta", "Lisa")
p = Pelota(16, "Amarillo", m)

#print(type(p.material))
print(p.material.nombre)