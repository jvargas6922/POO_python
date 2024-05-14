from pelota import Pelota


p = Pelota()

#ASIGNAR VALORES EN EL CUERPO DEL METODO
# print(p.color, p.tamanio, p.material)

#ASIGNAR VALORES DESDE LOS PARAMETROS DEL METODOS
# p = Pelota("Azul", 10, "Plástico")
# p2 = Pelota("Verde", 20, "Cuero")
# print(p.color, p.tamanio, p.material)
# print(p2.color, p2.tamanio, p2.material)

#ASIGNAR VALORES DESDE LOS PARAMETROS DEL METODO POR DEFECTO
# print(p.color, p.tamanio, p.material)
#print(p.color, p.tamanio_pelota, p.material)

#USO DE ACCESADOR
# print(p.color_y_material)
# print(p.tamanio)

#USO DE MODIFICADOR
#print(p.tamanio)
p.tamanio = 3
print(p.tamanio_pelota)

