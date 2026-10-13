#Crear un juego donde el jugador debe adivinar un numero secreto, se puede usar un ciclo while hasta que el jugador adivine el numero
#se puede usar la funcion randint para generar un valor aleatorio entre 1 y 50
#por cada intento fallido se debe incrementar una variable que lleve el conteo de intentos
#el programa debe orientar al jugardor indicandole que el valor que proporciono fue mayor o menor que el numero secreto
#si adivina el numero secreto debemos felicitar al usuario e indicarle cuantos intentos realizo
#y de modo opcional se puede limitar los intentos a maximo 10 de lo contrario termina el juego

from random import randint


print("\nAdivinando el numero".upper())
numero_secreto = randint(1 , 50)
intento = 0
adivinanza = None
intentos_maximos = 5

while adivinanza != numero_secreto and intento < intentos_maximos :
    adivinanza = int(input("Adivina el numero secreto (1 , 50): "))
    if adivinanza < numero_secreto:
        print("El numero secreto es mayo. ")
    elif adivinanza > numero_secreto:
        print("El numero secreto es menor.")
    intento += 1
if adivinanza == numero_secreto:
    print(f"Felicidades adivinaste el numero secreto en {intento} intentos. ")
else:
    print(f"Has superado los {intentos_maximos} intentos permitidos. ")
    print(f" El numero secreto era el: {numero_secreto}. ")