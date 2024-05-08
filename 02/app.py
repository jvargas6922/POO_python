from pelota import Pelota

pelota_jose = Pelota()
# print(pelota_jose)
# print(pelota_jose.forma)
# print(pelota_jose.material)
print(pelota_jose.color)
# print(pelota_jose.diametro)

#INSTANCIAS DE CLASE PELOTA
# pelota_futbol = Pelota()
# print(pelota_futbol.forma)
# print(pelota_futbol.material)
# print(pelota_futbol.color)
# print(pelota_futbol.diametro)

# pelota_tennis = Pelota()
# print(pelota_futbol.forma)
# print(pelota_futbol.material)
# print(pelota_futbol.color)
# print(pelota_futbol.diametro)

# pelota_andy = Pelota()
# print(pelota_futbol.forma)
# print(pelota_futbol.material)
# print(pelota_futbol.color)
# print(pelota_futbol.diametro)

#METODOS ESTÁTICO
# Pelota.rodar()
# Pelota.rebotar()
# Pelota.girar()
# accion = Pelota.crear_rebote()
# print(accion)


"""
class Pelota():
    forma = 'cuadrada, redonda,triangular'
    material = 'cuero, plastico, goma'
    color = 'blanco, negro, azul, etc'
    diametro = '10,22,30,50'
"""


#LLAMAR A NUESTRO METODO NO ESTATICO.
#LLAMAMOS METODO PARA CAMBIAR COLOR
pelota_jose.asignar_color('verde')
#LLAMAMOS METODO QUE NOS DA EL COLOR 
pelota_jose.leer_color()

pelota_jose.asignar_color('rojo')

pelota_jose.lee_color_local_y_atributo('rosado')

