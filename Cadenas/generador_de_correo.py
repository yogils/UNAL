#generador de correo
nombre = input("ingresa tu nombre: ")
edad = int(input("Cual es tu edad: "))
usuario = input("Cual es tu usuario normalizado: ")
empresa = input("nombre de la empresa: ")
dominio = input("Cual es el dominio de tu empresa: ")
extencion_dominio = input("Sabes cual es tu dominio de email?: ")
email_normalizado = input("sabes cual es tu dominio e email normalizado: ")

print(f"Hola denor {nombre}, Tu edad es {edad},Tu usuario asignado fue {usuario},Perteneces a la empresa {empresa},El dominio de la empresa es {dominio},Tu dominio de email es {extencion_dominio}")
print(f"Tu correo asignado es: {usuario}{email_normalizado}")





nombre_completo = input("Ingresa tu nombre complero: ")
normalizado = nombre_completo.strip()
nombre_usuario = nombre_completo.replace(" ",".")
nombre_usuario = nombre_usuario.lower()
empresa = input("ingrese el nombre de la empresa: ")
extencion_dominio = input("ingresa la extencion de dominio: ")
n_empresa_normaliado = empresa.replace(" ","").lower()
dominio_email = f"@{n_empresa_normaliado}{extencion_dominio}"
email = f"{nombre_usuario}{dominio_email}"
print(f"Su nombre completo es: {nombre_completo}")
print(f"su usuario es: {nombre_usuario}")
print(f"el nombre de la empresa es: {empresa}")
print(f"la extencion del dominio es: {extencion_dominio}")
print(dominio_email)
print("Su email es: ", email)
