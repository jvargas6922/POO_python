from orden_compa import OrdenCompra

oc = OrdenCompra()
oc.identificador = int(input("Ingrese el identificador de la orden de compra (OC) \n"))
oc.total_productos = int(input("Ingrese el total de productos \n"))
monto = int(input("Ingrese el monto de la compra \n"))
oc.asignar_monto(monto)
print(oc.codigo_descuento)

print(f"La orden de compra es: {oc.identificador} con un total de productos: {oc.total_productos} y un monto de: {oc.monto} con un codigo de descuento: {oc.codigo_descuento}")