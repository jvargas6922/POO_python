"""
MANEJO DE ERRORES Y EXCEPCIONES

TIPOS DE ERRORES
1- EXCEPCIONES
    SE PRODUCEN DURANTE LA EJECUCIÓN DEL PROGRAMA
2- ERRORES DE SINTAXIS
    SE PRODUCEN ANTES DE LA EJECUCIÓN DEL PROGRAMA

"""

#ERRORES DE SINTAXIS
# print("Hola Mundo)

#ERRORES DE EJECCUCIÓN
# print(10/0)

#ERRORES LOGICOS
# num_1 = input("Ingrese un número:\n ")
# num_2 = input("Ingrese un número:\n ")
# print(num_1 + num_2)

#MENEJO DE EXCEPCIONES
# try:
#     pass
# except:
#     pass
# finally:
#     pass

"""
TIPOS DE EXCEPCIONES
1- AttributeError => Atributo no encontrado
2- ImportError => Error al importar un módulo
3- IndexError => Índice fuera de rango
4- KeyError => Clave no encontrada
5- MemoryError => Error de memoria
6- NameError => Variable no encontrada
7- TypeError => Tipo de dato incorrecto
8- ZeroDivisionError => División por cero
"""

#BLOQUE TRY/EXCEPT
# consultar = True
# while consultar:
#     try:
#         edad = int(input("Ingrese su edad:\n"))
#         consultar = False
#     except ValueError:
#         print("Debe ingresar un numero")

#BLOQUE CON VARIAS EXCEPCIONES
# consultar = True
# while consultar:
#     try:
#         edad = int(input("Ingrese su edad:\n"))
#         divisor = int(input("Ingrese número para dividir su edad:\n"))
#         print(edad / divisor)
#         consultar = False
#     except ValueError:
#         print("Debe ingresar un número")
#     except ZeroDivisionError:
#         print("El N° por el cual desea dividir no puede ser cero")
#     except Exception as e:
#         print(f"ERROR: {e}")
#     except:
#         print("ERROR SIN INFORMACIÓN")


#LANZAMIENTO DE EXCEPCIONES
# consultar = True
# while consultar:
#     try:
#         edad = int(input("Ingrese su edad:\n"))
#         if edad < 0:
#             raise Exception("Edad debe ser un N° positivo.")
#         divisor = int(input("Ingrese número para dividir su edad:\n"))
#         print(edad / divisor)
#         consultar = False
#     except ValueError:
#         print("Debe ingresar un número")
#     except ZeroDivisionError:
#         print("El N° por el cual desea dividir no puede ser cero")
#     except Exception as e:
#         print(f"ERROR: {e}") 

#EXCEPCIONES DEFINIDAS POR EL USUARIO
from error import EdadError

# consultar = True
# while consultar:
#     try:
#         edad = int(input("Ingrese su edad:\n"))
#         if edad < 0:
#             raise EdadError("Debe ser un N° positivo.", edad)
#         divisor = int(input("Ingrese número para dividir su edad:\n"))
#         print(edad / divisor)
#         consultar = False
#     except ValueError:
#         print("Debe ingresar un número")
#     except ZeroDivisionError:
#         print("El N° por el cual desea dividir no puede ser cero")
#     except EdadError as e:
#         print(f"La edad '{e.edad}' no es válida. {e.mensaje}")
#     except Exception as e:
#         print(f"ERROR: {e}")

# ACCIONES DE LIMPIEZA
#EJEMPLO
intentos = 0
while intentos <= 3:
    try:
        edad = int(input("Ingrese su edad:\n"))
        if edad < 0:
            raise EdadError("Debe ser un N° positivo.", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except EdadError as e:
        print(f"La edad '{e.edad}' no es válida. {e.mensaje}")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        intentos +=1
        
#valores a ingresar
#25
#5
