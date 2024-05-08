from medicamento import Medicamento

primer_medicamento = Medicamento()
# print(primer_medicamento.descuento)
# print(primer_medicamento.IVA)

#METODOS ESTATICOS  
Medicamento.oferta()
# print(Medicamento.precio_final(100))
# print(Medicamento.precio_final_IVA(100))

#CASO1 => numero = -1
# numero = -1
# numero = 2
# numero = int(input("Ingrese un valor \n"))
# caso = Medicamento.validar_mayor_a_cero(numero)
# print(caso)
# print(f"{caso} el numero ingresado es:{numero}")

# m1 = Medicamento()
# m2 = Medicamento()

# if (m1.IVA == m2.IVA) and (m1.descuento == m2.descuento):
#     print("Los medicamentos tienen el mismo IVA y descuento")
# else:
#     print("no se cumplio la condicion")

#CASO PRECIO DE MEDICAMENTO
precio = int(input("Ingrese el precio del medicamento \n"))
# Medicamento.precio_final(precio)
# Medicamento.precio_final_IVA(precio)
# # print(f"El precio final del medicamento con descuento es: {Medicamento.precio_final(precio)}")
# print(f"El precio final del medicamento con descuento es: {Medicamento.precio_final_IVA(precio)}")

primer_medicamento.asigna_precio(precio)
print(primer_medicamento.descuento)




