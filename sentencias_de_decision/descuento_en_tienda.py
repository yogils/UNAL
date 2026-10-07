#Crear un sistema que ofrezca descuentos dependiendo el monto de la compra o si es miembro de la tienda.
print("BIENVENIDO A LA TIENDA DE DON PEPE")
print("hoy es dia de descuentos del si eres miemboro de la tienda o si tu compra es mayor a 100.000 pesos")

monto_de_compra = float(input("Ingrese el monto de su compra: "))
es_miembro = input("¿Eres miembro de la tienda? (Si/No): ").lower()

if monto_de_compra > 100000 and es_miembro == "si":
    print("¡Felicidades! Tienes un descuento del 10% en tu compra.")
    descuento = monto_de_compra * 0.10
    total_a_pagar = monto_de_compra - descuento
    print(f"El monto de tu compra es: {monto_de_compra} pesos")
    print(f"El descuento aplicado es: {descuento} pesos")
    print(f"El total a pagar es: {total_a_pagar} pesos")    
elif monto_de_compra < 100000 and es_miembro == "si":
    print("¡Felicidades! Tienes un descuento del 5% en tu compra.")
    descuento = monto_de_compra * 0.05
    total_a_pagar = monto_de_compra - descuento
    print(f"El monto de tu compra es: {monto_de_compra} pesos")
    print(f"El descuento aplicado es: {descuento} pesos")
    print(f"El total a pagar es: {total_a_pagar} pesos")
else:   
    print("Lo sentimos, no tienes derecho a ningún descuento en tu compra.")
    print("Te invitamos a hacerte miembro de nuestra tienda para disfrutar de descuentos exclusivos.")
    print(f"El monto de tu compra es: {monto_de_compra} pesos")
    print(f"El total a pagar es: {monto_de_compra} pesos")