"""
LEER UN ARCHIVO HTML 
"""

# OPCION 1
#pagina = open("index.html", 'r')
#print(pagina.read())
#pagina.close()

# OPCION 2
pagina = open("index.html")
lineas = pagina.readlines()
#print(lineas)

# OPCION 3
with open("index.html", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

# Cerrar el archivo
archivo.close()