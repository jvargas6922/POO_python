"""
EJERCICIO GUIADO MANJEJO DE ARCHIVOS
"""

import json

instancias = []

class Producto():
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

# Lectura y carga de productos desde el archivo
try:
    with open("productos.txt", "r") as productos:
        linea = productos.readline()
        while linea:
            producto = json.loads(linea)
            instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
            linea = productos.readline()
except FileNotFoundError:
    print("El archivo 'productos.txt' no existe.")
except json.JSONDecodeError:
    print("Error al leer un JSON del archivo.")

# Función para agregar un nuevo producto al archivo
def agregar_producto(nombre, precio):
    nuevo_producto = Producto(nombre, precio)
    instancias.append(nuevo_producto)
    with open("productos.txt", "a") as productos:
        productos.write(json.dumps({"nombre": nombre, "precio": precio}) + "\n")

# Ejemplo de uso
agregar_producto("Producto1", 10.99)
agregar_producto("Producto2", 5.49)

# Mostrar productos cargados
for producto in instancias:
    print(f"Producto: {producto.nombre}, Precio: {producto.precio}")