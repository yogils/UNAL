#Reserva de hotel
##
"""print("Bienvenido a nuestro hotel, por favor ingrese su nombre completo:")
nombre = input()
print("Ingrese su edad:")
edad = int(input())
print("Ingrese su país de residencia:")
pais = input()
print("Ingrese su estado civil:")   
estado_civil = input()
print("Desea reservar una habitación? (si/no)")
respuesta = input().lower()
if respuesta == "si":
    print("Ingrese el tipo de habitación que desea reservar (individual, doble, suite):")
    tipo_habitacion = input().lower()
    print("Ingrese la cantidad de noches que desea quedarse:")
    cantidad_noches = int(input())
    print("Ingrese el número de personas que se hospedarán:")
    cantidad_personas = int(input())
    print("Ingrese su correo electrónico para enviar la confirmación de la reserva:")
    correo_electronico = input()
    print("Gracias por su reserva. Se ha enviado un correo de confirmación a", correo_electronico)  
print("tarifa por noche de la habitación reservada:")   
tarifa_por_noche = float(input())
total_a_pagar = tarifa_por_noche * cantidad_noches
print("El total a pagar por su estadía es de:", total_a_pagar)
print("tiene vista al mar? (si/no)") 
vista_al_mar = input().lower()
if vista_al_mar == "si":
    print("Se le aplicará un cargo adicional por la vista al mar.")
    cargo_adicional = 50.0
    total_a_pagar += cargo_adicional
print("El total a pagar por su estadía con la vista al mar es de:", total_a_pagar)
print("Desea agregar servicios adicionales? (si/no)")
servicios_adicionales = input().lower()
if servicios_adicionales == "si":
    print("Ingrese los servicios adicionales que desea agregar (por ejemplo: desayuno, spa, transporte):")
    servicios = input()
    print("Ingrese el costo total de los servicios adicionales:")
    costo_servicios = float(input())
    total_a_pagar += costo_servicios
print("El total a pagar por su estadía con los servicios adicionales es de:", total_a_pagar)
print("Gracias por su reserva. Esperamos que disfrute su estadía en nuestro hotel.")      
"""""

print("\nBienvenido a nuestro hotel, por favor ingrese su nombre completo:")
nombre = "yohany alonso gil sanchez"
dias_de_estadia = 10
tarifa_diaria = 100.0
total_a_pagar = dias_de_estadia * tarifa_diaria
habitacion_con_vista_al_mar = True

print("Nombre del huésped:", nombre)
print("Días de estadía:", dias_de_estadia)
print("Tarifa diaria:", tarifa_diaria)
print("Total a pagar:", total_a_pagar)
print("Habitación con vista al mar?:", habitacion_con_vista_al_mar)

##datos modificados

print("\nBienvenido a nuestro hotel, por favor ingrese su nombre completo:")
nombre = "yohany andres lopez gil"
dias_de_estadia = 5
tarifa_diaria = 150.0
total_a_pagar = dias_de_estadia * tarifa_diaria
habitacion_con_vista_al_mar = False

print("Nombredel huesped:", nombre)
print("Dias de estadia:", dias_de_estadia)
print("Tarifa diaria:", tarifa_diaria)
print("Total a pagar:" , total_a_pagar)
print("Habitacion con vista al mar?:", habitacion_con_vista_al_mar)