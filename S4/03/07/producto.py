import json

instancias = []

class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

# Abre el archivo y lee todas las líneas
with open("productos.txt") as productos:
    for linea in productos:
        try:
            # Intenta cargar el objeto JSON desde la línea
            producto = json.loads(linea)
            # Agrega un nuevo Producto a la lista de instancias
            instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        except json.JSONDecodeError as e:
            print(f"Error al cargar JSON: {e}")

# Imprime los productos cargados
for instancia in instancias:
    print(f"Nombre: {instancia.nombre}, Precio: {instancia.precio}")
