#Vamos a crear un programa para realizar el calculo promedio de calificaciones.
#el programa debe solicitar el nimero de calificaciones a utilizar para obtener el promedio
#posteriormente, se debe solicitar cada calificacion al usuario
#posteriormente se debe generar una suma de calificaciones y mandar a imprimir un promedio
print("nuevo sistema de calificacion".upper())

calificaciones = []
n_calificaciones = int(input("Cuantas calificaciones desea adicionar => "))
for nota in range(n_calificaciones):
    calificacion = float(input(f"Indique la nota que desea agregar:{nota + 1} => "))
    calificaciones.append(calificacion)
total = sum(calificaciones)
total = total / n_calificaciones
print(calificaciones)
print(f"El promedio de sus calificaciones es: {total}")