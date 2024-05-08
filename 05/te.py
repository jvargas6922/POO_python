"""
ENTRADA 
     - formato_a = 300
     - formato_b = 500
    - tipo_a = te negro
    - tipo_b = te verde
    - tipo_c = infucion de hiervas
    - tiempo de preparacion_a = 3 min 
    - tiempo_preparacion_b = 5 min 
    - tiempo_preparacion_c = 6 min 
    - tiempo duracion = 1 año o 365 dias
    precio_a = 3000
    precio_b = 5000 
    - recomendacion_a = desayuno
    - recomendacion_b = medio dia
    - recomendacion_c = atardecer
    

PROCESO 


SALIDA

lista = [a, b, c]
         0, 1, 2

"""
class Te():
    formato =['300','500']
    tipo = ['Té negro','Té verde','Infución de hiervas']
    tiempo_preparacion = [3, 5, 6]
    tiempo_duracion = 1
    precio = [3000, 5000]
    recomendacion = ['Desayuno','Almuerzo','Cena']


    @staticmethod
    def presentacion(tipo_presentacion: int):
        if tipo_presentacion == 1:
            return Te.formato[0]
        else:
            return Te.formato[1]

    @staticmethod
    def tipo_te(te:int):
        if te == 1:
            return Te.tipo[0]
        elif te == 2: 
            return Te.tipo[1]
        else:
            return Te.tipo[2]

    @staticmethod
    def recomendacion_te(te:int): 
        if te == 1:
            return Te.recomendacion[0]
        elif te == 2: 
            return Te.recomendacion[1]
        else:
            return Te.recomendacion[2]
        
    @staticmethod
    def precio_te(tipo_presentacion:int):
        if tipo_presentacion == 1:
            return Te.precio[0]
        else:
            return Te.precio[1]