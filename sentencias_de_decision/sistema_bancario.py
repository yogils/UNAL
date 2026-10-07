#sistema bancaro
print("Bienvenido a bancolombia")
salir_sistema_txt = input("¿Desea salir del sistema? (si/no): ").lower()
if salir_sistema_txt == "si":
    print("Gracias por usar nuestro sistema bancario. ¡Hasta luego!")
else:
    print("¡Bienvenido al sistema bancario!")
    saldo = float(input("Ingrese su saldo actual: "))
    monto_retirar = float(input("Ingrese el monto que desea retirar: "))
    
    if monto_retirar <= saldo:
        saldo -= monto_retirar
        print(f"Retiro exitoso. Su nuevo saldo es: {saldo}")
    else:
        print("Saldo insuficiente para realizar el retiro.")