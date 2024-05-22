"""
EJEMPLO 1
"""

# modo lectura (por defecto)
archivo = open("prueba.txt")
# modo lectura, espeficado por el segundo argumento 'r'
historial = open("prueba.txt", 'r') 
print(archivo.read())