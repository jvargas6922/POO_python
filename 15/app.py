"""
Agregacion en Python
"""
from material import Material, Pelota

m = Material("Plastico", "corta", "Lisa")
p = Pelota(16, "Amarillo", m)

print(type(p.material))
print(p.material.nombre)