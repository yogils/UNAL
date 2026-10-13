#Ciclo de rango
print("Ciclo de rango")

for i in range (5):
    print(i, end=" ")

for i in range (1, 10,):
    print(i, end=" ")

for i in range (1, 10, 2):
    print(i, end=" ")

for i in range (0, 30, 2):
    print(i, end=" ")


mensaje = input("\nIngresa un mensaje que desees presentar: ")
n_repeticiones = int(input("\nIngresa un numero de veces que decea repetir: "))

for i in range(n_repeticiones):
    print(f"{i + 1} - {mensaje}")