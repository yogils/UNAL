#sistema de autenticacion de usuario
#crear un sistema para validar el nombre de usuario y la contraseña proporcionado por el usuario.
#se debe definir 2 constantes con el nombre de usuario y la contraseña correctos, y luego comparar los valores ingresados por el usuario con estas constantes. Si ambos coinciden, se debe mostrar un mensaje de bienvenida, de lo contrario, se debe mostrar un mensaje de error.
print("SISTEMA DE AUTENTICACION DE USUARIO")
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")
us = "admin"
ps = "1234"   

if usuario == us and contrasena == ps:
    print(f"¡Bienvenido al sistema , {usuario}!")
elif usuario != us and contrasena == ps:    
    print("Error: Nombre de usuario incorrecto.")
elif usuario == us and contrasena != ps:
    print("Error: Contraseña incorrecta.")
else:
    print("Error: Nombre de usuario y contraseña incorrectos.")