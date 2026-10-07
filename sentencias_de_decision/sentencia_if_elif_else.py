#Sentencia if, elif, else
print("SENTENCIA IF")

edad = int(input("Ingrese su edad: "))
if edad <= 10:
    print(f"Usted es un niño. tienes {edad} años")

elif 11 <= edad <= 17:
    print(f"Usted es un adolescente. tienes {edad} años")

elif edad <= 59:
    print(f"Usted es un adulto joven. tienes {edad} años")

else:
    print(f"Usted es un adulto. tienes {edad} años")


#Validador numero positivo, negativo o cero
print("VALIDADOR DE NUMERO")

numero = int(input("Ingese un numero: "))
if numero > 0:
    print(f"el {numero} es un numero positivo.")
elif numero < 0:
    print(f" El {numero} es un numero negativo.")
else:
    print(f"El {numero} es cero.")

#Operador ternario
print("OPERADOR TERNARIO")
edad = int(input("Ingrese su edad: "))
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje) 

#sistema de el numero mayor de dos numeros
print("SISTEMA DE NUMERO MAYOR DE DOS NUMEROS")
numero1 = int(input("Ingrese el primer numero: ")) 
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 > numero2:           
    print(f"El numero mayor es: {numero1}") 
else:
    print(f"El numero mayor es: {numero2}") 
