#Ahora vamos a generar un programa que nos genere un correo aleatorio para nuestra compania
from random import randint


print("BIENVENIDO A NUESTRO PROGRAMA PARA GENERAR TU CORREO")
nombre = input("Por favor digita tu nombre: ")
apellido = input("Ingresa tu apellido: ")
empresa = input("Digita el nombre de tu empresa: ")
ext_dominio = input("Ingresa la extencion de dominio")
nnombre = nombre.lower()[:3]
napellido = apellido.lower()[:3]
aleatorio = randint(100, 999)
dominio_email = f"@{empresa.replace(' ','.')}{ext_dominio}"
email = f"{nnombre}{napellido}{aleatorio}{dominio_email}"

print(f"Bienvenido a la empresa: {empresa.upper()} senor: {nombre.upper()} {apellido.upper()} \nNos complace informarte que su correo ya fue creado y quedara con la siguiente direccion: {email.lower()} ")