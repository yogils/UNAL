#Cambiar entre mayusculas y minusculas
nombre = "yohany alonso gil sánchez"
print("Nombre en minusculas:", nombre.lower())
print("Nombre en mayusculas:", nombre.upper())
print("Nombre con primera letra en mayuscula:", nombre.title())

#Cambiar entre mayusculas y minusculas en un texto largo
mensaje = """Mi nombre es yohany alonso gil sánchez, tengo 36 años, vivo en Colombia y soy estudiante: True 
Lo mas duro de estudiar en Medellin es tener que bajar en la moto a la universidad y luego subir a la moto para regresar a casa, pero lo    mas duro es que en el camino me encuentro con muchos semaforos y trancones,         
lo que hace que pierda mucho tiempo en el trafico"""
print("\nMensaje en minusculas:", mensaje.lower(), len(mensaje.lower()))
print("\nMensaje en mayusculas:", mensaje.upper(), len(mensaje.upper()))  
print("\nMensaje con primera letra en mayuscula:", mensaje.title() , len(mensaje.title()))

