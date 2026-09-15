#Concatenar cadenas
print("\nConcatenar cadenas usando el +")
nombre = "Yohany"
apellido = "Gil"
n_completo = nombre + " " + apellido
print("Mi nombre es " + n_completo)

#solo. con el metodo print() se puede concatenar cadenas sin el uso del operador +
print("\nConcatenar cadenas usando el metodo print()")
edad = 36
pais = "Colombia"   
print("Mi nombre es", n_completo, "tengo", edad, "años y vivo en", pais)

#Concatenar cadenas usando f-strings
print("\nConcatenar cadenas usando f-strings")
estudio = "Ingenieria de Sistemas"  
trabajo = "Desarrollador de Software"
presentacion = f"Mi nombre es {n_completo}, tengo {edad} años, vivo en {pais}, estudio {estudio} y trabajo como {trabajo}."
print(presentacion)