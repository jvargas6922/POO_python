from televisor import Televisor, televisorLed, Monitores_Multifuncion

print("Programa para practicar herencia en Python")
print("==========================================")
marca = input("Ingrese la marca del televisor: ")
modelo = input("Ingrese el modelo del televisor: ")
pulgadas = float(input("Ingrese las pulgadas del televisor: "))

televisor = Televisor(marca, modelo, pulgadas)
print("Televisor creado con éxito")

televisorLed = televisorLed(marca, modelo, pulgadas)
print("Televisor LED creado con éxito")

monitores = Monitores_Multifuncion(marca, modelo, pulgadas)
print("Monitor multifunción creado con éxito")
print("==========================================")



