#Generador de valores aleatorios
import random
from random import randint
print("Ahora vamos a crear un programa que nos generen valores aleatorios")

numero = randint(1, 100)
print(numero)

numero2 = random.sample(range(1, 200),3)
print(numero2)


dado1 = randint(1, 6)
dado2 = randint(1, 6)
print(f"Al tirar los dados los resultados son los siguientes:\n{dado1}\n{dado2}")

#sistema generador de id unico
print("BIENVENIDO AL SISTEMA DE GENERADOR DE ID UNICO")
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
ano_nacimiento = input("Ingresa tu ano de nacimiento: ")
nombre1 = nombre.upper()[:2]
apellido1 = apellido.upper()[:2]
ano_nacimiento1 = ano_nacimiento[2:]
aleatorio = randint(1000,  9999)
print(f"Sus datos son los siguientes: \nSu nombre es: {nombre.upper()} \nSu apellido es:{apellido.upper()}, \nNaciste en el anio:{ano_nacimiento}")
print(f"Su id unico generado por el sistema es: {nombre1}{apellido1}{ano_nacimiento1}{aleatorio}")