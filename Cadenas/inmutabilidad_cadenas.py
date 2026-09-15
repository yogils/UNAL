#Inmutabiliidad de las cadenas
#Las cadenas son inmutables, lo que significa que no se pueden cambiar una vez que se han creado. Cualquier operación que modifique una cadena en realidad crea una nueva cadena.
#Ejemplo de inmutabilidad de las cadenas
"""print("\nInmutabilidad de las cadenas")
nombre = "Yohany Alonso Gil Sanchez"
print("Nombre original:", nombre)
#Intento de modificar la cadena
nombre[0] = "J"  # Esto generará un error, ya que las cadenas son inmutables
print("Nombre modificado:", nombre) """

#Pero podemos adicionar elementos en cadenas usando concatenacion
print("\nAdicionar elementos en cadenas usando concatenacion")  
animal = "perro"
print("Animal original:", animal)
#Concatenar una nueva cadena al final de la cadena original
animal = animal + "s"
print("Animal modificado:", animal)

plural1 = animal + "s" + " "+ "grandes"
print("Animal plural:", plural1)
