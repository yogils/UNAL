#sistema de calificaciones
#crear un sistema para convertir una calificacion numerica entre 0 y 10 a una calificacion literal (A, B, C, D, F) segun la siguiente escala:
#A: 9-10
#B: 8-8.9   
#C: 7-7.9   
#D: 6-6.9   
#F: 0-5.9   
print("SISTEMA DE CALIFICACIONES")  
calificacion = float(input("Ingrese su calificación (0-10): "))

if 9 <= calificacion <= 10:
    print("Su calificación es: A")
elif 8 <= calificacion < 9:
    print("Su calificación es: B")
elif 7 <= calificacion < 8:
    print("Su calificación es: C")
elif 6 <= calificacion < 7:
    print("Su calificación es: D")
else:
    print("Su calificación es: F")  


#sistemade envios 
#crear un sistema que determine el costo de envio de un paquete segun su peso y destino.    
print("SISTEMA DE ENVIO DE PAQUETES")
peso = float(input("Ingrese el peso del paquete (en kg): "))    
destino = input("Ingrese el destino del paquete (nacional/internacional): ").lower()

valor_kilo = 10000
destino_nacional = 5000
destino_internacional = 15000

valor_envio = peso * valor_kilo

if destino == "nacional":
    valor_envio += destino_nacional
elif destino == "internacional":
    valor_envio += destino_internacional

print(f"El costo de envío es: ${valor_envio}")  