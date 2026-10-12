#Cajero automatico

print("BIENVENIDO AL CAJERO ESPERO ESTE MUY BIEN")
clave = 1234
saldo = 1000000
salir = True
while salir == True:
    print(f"""Menu:
    1. Consultar saldo
    2. Retirar dinero
    3. Hacer pagos
    4. Hacer consignacion
    5. Salir
""")
    opcion = int(input("Por favor elija una opcion: "))
    if opcion == 1:
        print(f"""menu:
        1. consultar saldo
        2. Regresar al menu anterior
        """)
        subopcion = int(input("elija una opcion: "))
        if subopcion == 1:
            clave_usuario = int(input("digita tu clave: "))
            if clave_usuario != clave:
                print("su clave no es correcta")
                while clave_usuario != clave:
                    clave_usuario = int(input("Ingresa de nuevo la clave: "))
                    if clave_usuario == clave:
                        print(f"tu cuenta es de {saldo}: ")

    elif opcion == 2:
        saldo_retirar = int(input("Ingresa la cantidad a retirar: "))
        clave_usuario = int(input("digita tu clave: "))
        saldo = saldo - saldo_retirar
        while clave_usuario != clave:
            print("su clave no es correcta")
            clave_usuario = int(input("Ingresa de nuevo la clave: "))
        if saldo_retirar > saldo:
            print("El saldo que intentas retirar es mayor que el saldo de tu cuenta.")
        elif saldo_retirar == 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        else:
            print(f"Hemos procesado tu retiro, tu saldo ahora de {saldo}")
    elif opcion == 3:
        pd_a_pagar = input("Igrese el producto a pagar: ")
        valor = int(input("Ingrese el valor a pagar: "))
        if valor > saldo:
            print("No cuentas con saldo suficiente en la cuenta.")
        else:
            print(f"Su {pd_a_pagar} se  pago con exito, muchas gracias por usar nuestro servicio.")
    elif opcion == 4:
        saldo_consignar = int(input("Ingresa el saldo a consignar: "))
        clave_usuario = int(input("digita tu clave: "))    
        saldo = saldo +saldo_consignar 
        while clave_usuario != clave:
            print("su clave no es correcta")
            clave_usuario = int(input("Ingresa de nuevo la clave: ")) 
        if saldo_consignar <= 0:
            print("El saldo que deseas consignar no puede ser 0:") 
        else:
            print(f"Tu nuevo saldo es de: {saldo}")
    elif opcion == 5:
        print("Gracias por usar nuestro sistema Bancario. ")
        salir = False
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
        