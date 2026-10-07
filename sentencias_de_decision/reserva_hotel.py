
#Reserva de hotel

print("BIENVENIDO A NUESTRO HOTEL TRANSILVANIA")

nombre_huesped = input("ingresa tu nombre:  ")
edad_huesped = int(input("ingresa tu edad:  "))
dias_de_estadia = int(input("ingresa la cantidad de dias que te quedaras:  "))
habitacion_con_vista_al_mar = input("¿Deseas una habitacion con vista al mar? (Si/No): ").lower()
habitacion_con_desayuno_incluido = input("¿Deseas una habitacion con desayuno incluido? (Si/No): ").lower()
habitacion_cama_doble = input("¿Deseas una habitacion con cama doble? (Si/No): ").lower()
acompanante = input("¿Vas a ir acompañado? (Si/No): ").lower()

vista_al_mas = 300000
sin_vista_al_mar = 200000
desayuno_incluido = 50000
cama_doble = 100000

vista_al_mar_total = dias_de_estadia * vista_al_mas
sin_vista_al_mar_total = dias_de_estadia * sin_vista_al_mar
desayuno_incluido_total = dias_de_estadia * desayuno_incluido
cama_doble_total = dias_de_estadia * cama_doble

if edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "si" and acompanante == "si":
    total_a_pagar = vista_al_mar_total + desayuno_incluido_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "si" and acompanante == "no":
    total_a_pagar = vista_al_mar_total + desayuno_incluido_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "no" and acompanante == "si":
    total_a_pagar = vista_al_mar_total + desayuno_incluido_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "no" and acompanante == "no":
    total_a_pagar = vista_al_mar_total + desayuno_incluido_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "si" and acompanante == "si":
    total_a_pagar = vista_al_mar_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "si" and acompanante == "no":
    total_a_pagar = vista_al_mar_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "no" and acompanante == "si":
    total_a_pagar = vista_al_mar_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "si" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "no" and acompanante == "no":
    total_a_pagar = vista_al_mar_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "si" and acompanante == "si":
    total_a_pagar = sin_vista_al_mar_total + desayuno_incluido_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "si" and acompanante == "no":
    total_a_pagar = sin_vista_al_mar_total + desayuno_incluido_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "no" and acompanante == "si":
    total_a_pagar = sin_vista_al_mar_total + desayuno_incluido_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "si" and habitacion_cama_doble == "no" and acompanante == "no":
    total_a_pagar = sin_vista_al_mar_total + desayuno_incluido_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "si" and acompanante == "si":
    total_a_pagar = sin_vista_al_mar_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "si" and acompanante == "no":
    total_a_pagar = sin_vista_al_mar_total + cama_doble_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "no" and acompanante == "si":
    total_a_pagar = sin_vista_al_mar_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped >= 18 and habitacion_con_vista_al_mar == "no" and habitacion_con_desayuno_incluido == "no" and habitacion_cama_doble == "no" and acompanante == "no":
    total_a_pagar = sin_vista_al_mar_total
    print(f"El total a pagar por tu estadia es: {total_a_pagar} pesos")
elif edad_huesped < 18 and acompanante == "si":
    print("bienvenido a nuestro hotel, pero te recomiendo no quedarte solo ya que eres menor de edad.")
else:
    print("Lo siento, no puedes quedarte en nuestro hotel ya que eres menor de edad y no tienes acompañante.")




















"""print("BIENVENIDO A NUESTRO HOTEL TRANSILVANIA")

nombre_huesped = input("Ingresa tu nombre: ")

edad_huesped = int(input("Ingresa tu edad: "))

dias_de_estadia = int(input("Ingresa la cantidad de días que te quedarás: "))

habitacion_con_vista_al_mar = input(
    "¿Deseas una habitación con vista al mar? (Si/No): "
).lower()

habitacion_con_desayuno_incluido = input(
    "¿Deseas una habitación con desayuno incluido? (Si/No): "
).lower()

habitacion_cama_doble = input(
    "¿Deseas una habitación con cama doble? (Si/No): "
).lower()

acompanante = input(
    "¿Vas a ir acompañado? (Si/No): "
).lower()


# PRECIOS

vista_al_mar = 300000
sin_vista_al_mar = 200000
desayuno = 50000
cama_doble = 100000


# VERIFICAMOS SI ES MAYOR DE EDAD

if edad_huesped >= 18:

    # Precio de la habitación
    if habitacion_con_vista_al_mar == "si":
        total_a_pagar = dias_de_estadia * vista_al_mar
    else:
        total_a_pagar = dias_de_estadia * sin_vista_al_mar


    # Desayuno
    if habitacion_con_desayuno_incluido == "si":
        total_a_pagar += dias_de_estadia * desayuno


    # Cama doble
    if habitacion_cama_doble == "si":
        total_a_pagar += dias_de_estadia * cama_doble


    # Resultado
    print()
    print(f"Hola {nombre_huesped}")
    print(f"El total a pagar por tu estadía es: {total_a_pagar} pesos")


# SI ES MENOR DE EDAD

elif acompanante == "si":

    print()
    print(
        "Bienvenido a nuestro hotel, pero te recomiendo "
        "no quedarte solo ya que eres menor de edad."
    )

else:

    print()
    print(
        "Lo siento, no puedes quedarte en nuestro hotel "
        "ya que eres menor de edad y no tienes acompañante."
    )
"""