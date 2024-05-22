import time


try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")

"""
pasos:
1 correr el codigo
2 ingresar un valor que no sea un numero
3 revisar el archivo de log

"""

