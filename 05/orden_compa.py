class OrdenCompra():

    def nueva_orden(self):
        #se dfeine los atributos
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0
        self.codigo_descuento = ""

    def asignar_monto(self, nueevo_monto:int):
        self.monto = nueevo_monto
        self.codigo_descuento = ''

        if self.monto > 20000:
            self.codigo_descuento = "20PORCIENTO"
        elif self.monto > 10000:
            self.codigo_descuento = "10PORCIENTO"