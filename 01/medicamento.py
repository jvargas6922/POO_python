"""
PROGRAMACION ORIENTADA A OBJETOS
DEFINICION DE CLASES: UNA CLASE ES UNA PLANTILLA PARA CREAR OBJETOS
DEFINICION DE OBJETOS: UN OBJETO ES UNA INSTANCIA DE UNA CLASE
ATRIBUTOS: SON LAS CARACTERISTICAS DE UN OBJETO
METODOS: SON LAS ACCIONES QUE UN OBJETO PUEDE REALIZAR
"""

# DEFINICION DE CLASE
class Medicamento():
    #ATRIBUTOS
    descuento = 0.10
    #IVA ES UNA ATRIBUTO PERO TAMBIEN COMO LO ESCRIBIMOS EN MAYUSCULA ES UNA CONSTANTE
    IVA = 0.19
    precio = 0

    #METODOS ESTATICOS
    @staticmethod
    def oferta():
        print("OFERTA DEL DIA: 10% DE DESCUENTO")

    @staticmethod
    def precio_final(precio):
        return precio - (precio * Medicamento.descuento)
    
    @staticmethod
    def precio_final_IVA(precio):
        return precio + (precio * Medicamento.IVA)
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        # return numero > 0
        #CASO1 => numero = -1
        #CASO2 => numero = 2
        if numero > 0:
            return "Dato valido"
        else:
            return "Dato invalido"
        
    #METODOS DE INSTANCIA
    #def precio_final_2(Medicamento, precio:int):
    def precio_final_2(self, precio:int):
        return precio - (precio * self.descuento)
    
    def asigna_precio(self, precio):
        valor = self.validar_mayor_a_cero(precio)
        if valor == "Dato valido":
            self.precio = precio
            if self.precio >= 1000 and self.precio <= 20000:
                self.descuento = 0.1
            elif self.precio > 20000 and self.precio <= 30000:
                self.descuento = 0.2
            elif self.precio > 30000:
                self.descuento = 0.3
            print(f"El precio ingresado es valido {self.precio}")

        else:
            print(f"El precio ingresado no es valido precio inicial{self.precio}")   

    