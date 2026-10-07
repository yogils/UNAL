#acumulador suma usando while
print("ACUMULADOR SUMA USANDO WHILE")
maxumo = 5
numero = 1
acumulador = 0
while numero <= maxumo: 
    print(f"Numero: {numero} + {acumulador}")
    acumulador += numero
    numero += 1
print(f"La suma de los numeros del 1 al {maxumo} es: {acumulador}") 