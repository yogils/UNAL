#Vamos a realizar una calculadora
print("Bienvenidos a nuestra calculadora")

salir = True
while salir == True:
    print(f"""Menu
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
""")
    opcion = int(input("Por favor ingrese una de las siguientes opciones: "))
    valor1 = int(input("Ingresa un primer numero: "))
    valor2 = int(input("Ingresa un segundo numero: "))
    if opcion == 1:
        Suma = valor1 + valor2
        print(f" El total de la sumas es: {Suma}")
        salir = False
    elif opcion == 2:
        Resta = valor1 - valor2
        print(f"El valor de la resta es: {Resta:.2f}")
        salir = False
    elif opcion == 3:
        Multiplicacion = valor1 * valor2
        print(f"El total de la multiplicacion es: {Multiplicacion}")
        salir = False
    elif opcion == 4:
        Division = valor1 / valor2
        print(f"El valor de la dicion es: {Division}")
        salir = False
    else:
        print("Gracias por usar nuestra calculadora.")
        salir = False