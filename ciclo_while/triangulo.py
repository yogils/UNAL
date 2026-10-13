#triangulo
print("Vamos a crear un triangulo")

numero_filas = int(input("Proporcina el numero de filas. "))

for fila in range (1, numero_filas + 1):
    espacio_en_blanco = " " * (numero_filas - fila)
    asterisco = "*" * (2 * fila - 1)
    print(f"{espacio_en_blanco}{asterisco}")