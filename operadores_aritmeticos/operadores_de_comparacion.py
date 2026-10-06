#Operadores de comparacion
# ==, !=, >, <, >=, <=
print("Operadores de comparacion")
a = 10
b = 20
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

#operadores logicos
# and, or, not
print("Operadores logicos")
x = True
y = False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")    

#sistema de descuento VIP

print("Sistema de descuento VIP")
numero_de_compras = 15
cantidad_de_productos = int(input("Ingrese la cantidad de productos comprados: "))
tienes_membresia_vip = input("¿Tienes membresía VIP? (si/no): ")

elegible_descuento = numero_de_compras > 10 and cantidad_de_productos > 5 and tienes_membresia_vip.lower() == "si"
print(f"¿Elegible para descuento VIP? {elegible_descuento}")
