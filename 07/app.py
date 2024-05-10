"""
EJERCICIO GUIADO MODULO2
"""
from medicamento import Medicamento

nombre = input("Ingrese el nombre del medicamento: ")
stock = int(input("Ingrese el stock del medicamento: "))
precio_bruto = int(input("Ingrese el precio bruto del medicamento: "))

m1 = Medicamento(nombre, stock)
m1.precio = precio_bruto

print(f"El precio bruto del medicamento {m1.nombre} es: {m1.precio_bruto}")

if m1.descuento:
    print(f"El medicamento {m1.nombre} tiene un descuento del {m1.descuento * 100}%")

print(f"El precio final del medicamento {m1.nombre} es: {m1.precio_final}")