from te import Te

te = Te()

print('Bienvenidos Tienda Té')
print('Tenemos para ofecerle los siempres tipos de Té')
print('1- Té Negro\n2- Té Verde\n3- Infución de Hiervas')

tipo_te = int(input("Seleccione el tipo de Té: (1)-(2)-(3)\n"))
te_seleccionado = Te.tipo_te(tipo_te)

print('Existen Presentacion \n 1- 300gr \n 2- 500gr')
#USUARIO SELECCIONA PRESENTACION
presentacion = int(input("Que presentacion seleccionas:(1)-(2) \n"))
presentacion_seleccionada = Te.presentacion(presentacion)

precio_presentacion = Te.precio_te(presentacion)
recomendacion_te = Te.recomendacion_te(tipo_te)

print(f"El usuario seleccion:\n{te_seleccionado} en la presentación de {presentacion_seleccionada}\nse recomienda tomarlo {recomendacion_te}\n y su precio es ${precio_presentacion}\ngracias por su compra")