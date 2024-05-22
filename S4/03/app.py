import os
# log_file = open(os.path.abspath("logs/error.log"))

# archivo = open("ejemplo.txt", "r")
# print(archivo.read())

# pagina = open("index.html", "r")
# lineas = pagina.readlines()
# print(lineas)
# # print(pagina.read())

# with open("index.html", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())


# import time
# try:
#     edad = int(input("Ingrese su edad:\n"))
# except Exception as e:
#     with open(f"{round(time.time())}.log", "w") as log:
#         log.write(f"ERROR: {e}")



# from datetime import datetime
# try:
#     edad = int(input("Ingrese su edad:\n"))
# except Exception as e:
#     with open("error.log", "a+") as log:
#         log.seek(0)
#         print(log.read())
#         now = datetime.now()
#         log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
#         log.seek(0)
#         print(log.read())

# with open("error.log") as log:
#     log.seek(0)
#     print(log.read(10))

# with open("error.log") as log:
#     log.seek(10)
#     print(log.read(10))
#     print(log.read(10))

import os
from datetime import datetime

def obtener_datos():
    nombre = input("Ingrese su nombre:\n")
    edad = int(input("Ingrese su edad:\n"))
    email = input("Ingrese su correo electrónico:\n")
    return nombre, edad, email

def registrar_datos(nombre, edad, email):
    with open("data.log", "a+") as data_file:
        data_file.write(f"Nombre: {nombre}, Edad: {edad}, Email: {email}\n")
        print("Datos registrados exitosamente.")

try:
    nombre, edad, email = obtener_datos()
    registrar_datos(nombre, edad, email)
except ValueError as ve:
    print("Error: La entrada no es válida.")
    with open("error.log", "a+") as log:
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {ve}\n")
        print("Error registrado en el archivo 'error.log'.")
except Exception as e:
    print("Se produjo un error inesperado:", e)



