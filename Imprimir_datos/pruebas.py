"""#esta es la formula para imprimir en pantalla#
print("hola mundo, soy yohany el mejor programador del mundo")

r  = 9 + 20 / 2**2 - (7//3 + 1)
print(r)

a = 10
b = 5
c = a
a = b
b = c
c = 10

print("el valor de a es:", a)
print("el valor de b es:", b)   
print("el valor de c es:", c)  """ 

"""nombre = input()
edad = int(input())
peso = float(input())

print(f"Mi nombre es: {nombre} y tengo {edad} años y peso {peso} kilos")"""

"""R = float(input())

W = R * 0.19
T = R * 0.10
U = R + W + T

print("Total consumido: COP$", R)
print("Valor IVA: COP$", W)
print("Valor propina: COP$", T)
print("A pagar: COP$", U)"""



from math import sqrt
import string
from datetime import date

"""r = float(input())

perimetro = 2 * math.pi * r
area = math.pi * r**2
volumen = (4/3) * math.pi * r**3

print("Perimetro: ", perimetro)
print("Area: ", area)
print("Volumen: ", volumen) """


"""import math  
l = float(input())
d = float(input())  

l2 = math.sqrt((d**2) - (l**2))
area = l * l2
print(f"{area:.2f}")"""

# multiplo de 5

"""n = int(input("Ingrese un número: "))
if n % 5 == 0:
    print(f"{n} es múltiplo de 5")
else:
    print(f"{n} no es múltiplo de 5")"""
"""# el premio
a = int(input("Ingrese un número: "))
b = "bicicleta"
l = "licuadora"
an = "ancheta"
if a > 0:
    print(b)
elif a == 0:
    print(l)
else:
    print(an)"""

#almacen de descuento
"""valor = int(input())
cantidad = int(input())

total = valor * cantidad

if cantidad <= 2:
    total = total
elif cantidad <= 5:
    total = total - (total * 10 // 100)
elif cantidad <= 10:
    total = total - (total * 15 // 100)
else:
    total = total - (total * 20 // 100)

print("El total a pagar por el cliente es $" + str(total))"""


""""""

"""h = int(input())
valor_hora = int(input())
total = h * valor_hora

if h <= 5:
    total = total - (total*60//100)
else:
    primeras_5 = 5 * valor_hora
    primeras_5 = primeras_5 - (primeras_5 * 60 // 100)
    hora_adicional = h - 5
    adicional = hora_adicional * valor_hora
    adicional = adicional + (adicional * 150 //100)
    total = primeras_5 +adicional


print("$"+ str (total))
"""
"""#calcualr la ecucion velocidad = distancia sobre tiempo D T V

M1 = input()
V1 = float(input())

M2 = input()
V2 = float(input())

if M1 == "D" and M2 == "T":
    M3 = V1 / V2
    R = "V"
elif M1 == "T" and M2 == "D":
    M3 = V2 / V1
    R = "V"
elif M1 == "V" and M2 == "T":
    M3 = V1 * V2
    R = "D"
elif M1 == "T" and M2 == "V":
    M3 = V2 * V1
    R = "D"
elif M1 == "V" and M2 == "D":
    M3 = V2 / V1
    R = "T"
elif M1 == "D" and M2 == "V":
    M3 = V1 / V2
    R = "T"
print(f"{R} = {M3:.1f}")
"""
"""#Gastos a fin de mes

saldo_en_cuenta = int(input())
gastos_del_mes = int(input())

if saldo_en_cuenta < gastos_del_mes :
    print("No llegas a fin de mes")
else:
    print("Si llegas a fin de mes")"""

"""#ajedrez

fila = int(input())
columna = int(input())

if (fila + columna) % 2 == 0:
    print("NEGRO")
else:
    print("BLANCO")"""

""""#Triangulo
lado_A = float(input())
lado_B = float(input())
lado_C = float(input())

if (lado_A + lado_B > lado_C) and (lado_A + lado_C > lado_B) and (lado_B + lado_C > lado_A):

    if lado_A == lado_B and lado_B == lado_C:
        print("Los lados ingresados conforman un triangulo equilatero")
    elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
        print("Los lados ingresados conforman un triangulo isosceles")
    else:
        print("Los lados ingresados conforman un triangulo escaleno")
else:
    print("Los lados ingresados no conforman un triangulo")"""

"""#Dias del mes

mes = input("")
dia = int(input())

if (mes == "Enero") or (mes == "febrero") or (mes =="Marzo" and dia < 20):
    print("Invierno")
elif (mes == "Marzo" and dia >=20) or (mes == "Abril") or (mes == "Mayo") or (mes == "Junio" and dia < 21):
    print("Primavera")
elif (mes =="junio" and dia >= 21) or (mes == "Julio") or (mes == "Agosto") or (mes ==" Septiembre" and dia < 22):
    print("Verano")
elif (mes == "Septiembre" and dia >= 21) or (mes == "Octubre") or (mes == "Noviembre") or (mes == "Diciembre" and dia < 21):
    print("Otono")
else:
    print("Invierno")
"""

"""#rayita"""

"""Andrea = float(input())
Sandra = float(input())
Milena = float(input())

if (Andrea > Sandra and Andrea < Milena ) or (Andrea < Sandra and Andrea > Milena):
    print("Gana Andrea")
elif (Sandra > Andrea and Sandra < Milena) or (Sandra < Andrea and Sandra > Milena):
    print("Gana Sandra")
else:
    print("Gana Milena")"""

"""# salario empleado
horas = int(input())
valor_hora = int(input())

if horas <= 40:
    salario = horas * valor_hora
elif horas <= 48:
    salario = (40 * valor_hora) + ((horas - 40) * valor_hora * 2)
else:
    salario = (40 * valor_hora) + (8 * valor_hora * 2) + ((horas - 48) * valor_hora * 3)

print(f"El empleado recibira un salario de ${salario}")"""

"""M = int(input())
N = int(input())

for i in range(1, N + 1):
    print(M, "x", i, "=", M * i)"""
"""#Cultivo de bacterias

individuos = float(input())

horas = 0

while individuos >= 10:
    individuos = individuos / 2
    horas += 1
print(horas)"""

"""#Cuadrado
n = int(input())
l = float(input())
suma = l* l
for i in range (n-1):
    val = float(input())
    l+=val
    suma+=l*l
print(f"Ramon, el area total de la estructura basica del universo es de {round(suma,2)} centimetros cuadrados")
"""
#capacidad de carga

"""capacidad_de_carga = float(input())
bultos = int(input())
suma = 0
cantidad = 0
for i in range(bultos):
    bultos = float(input())
    cantidad+=bultos
    if (cantidad <= capacidad_de_carga):
        suma =+ 1
    else:
        break
print(f"Caben {suma} bultos de papa")"""

"""n = int(input())
sum = 17
print(sum)
for i in range(1,n+1):
    if(i%2==1):
        sum -= 2
        print(sum)
    else:
        sum+=3
        print(sum)"""

"""n = int(input())
sum = 0
for i in range(n):
    val = int(input())
    es_primo = True

    if val <= 1:
        es_primo = False
    else:
        for d in range (2, val):
            if val % d == 0:
                es_primo = False
                break
    if es_primo:
        sum += 1
print(sum)
"""