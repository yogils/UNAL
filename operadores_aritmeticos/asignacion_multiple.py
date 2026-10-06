#Asignación Múltiple
print("Asignación Múltiple")

a, b, c = 5, 10, 15
print(f"a = {a}, b = {b}, c = {c}")

nadar, correr, saltar = "natación", "atletismo", "saltar"
print(f"nadar = {nadar}, correr = {correr}, saltar = {saltar}")

#asignacion encadenada
x = y = z = 20
print(f"x = {x}, y = {y}, z = {z}")

suma = x + y + z
print(f"la suma de x, y, z es: {suma}")

#intercambio de valores en variables
x, y, z = 10, 20, 30
print(f"antes del intercambio: x = {x}, y = {y}, z = {z}")

x, y, z = z, x, y
print(f"despues del intercambio: x = {x}, y = {y}, z = {z}")