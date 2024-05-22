from datetime import datetime






try:
    # INGRESO DE DATOS
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    # REGISTRO DE ERROR
    with open("error.log", "a+") as log:
        # SEEK PARA MOVER EL CURSOR DE LECTURA/ESCRITURA
        log.seek(0)
        # IMPRIMIR EL CONTENIDO DEL ARCHIVO
        print(log.read())
        # ESCRIBIR EN EL ARCHIVO
        now = datetime.now()
        # FORMATO DE FECHA
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        # MOVER EL CURSOR AL INICIO DEL ARCHIVO
        log.seek(0)
        # IMPRIMIR EL CONTENIDO DEL ARCHIVO
        print(log.read())



"""
EJECUCION:
1. CORRER EL CODIGO
2. INGRESAR UN VALOR QUE NO SEA UN NUMERO

"""