#Suatema para saber en que estacion del año estamos 
print("Bienvenido al sistema de estaciones del año")
mes = input("Ingrese el mes actual (por ejemplo, enero, febrero, marzo, etc ): ").lower()   

if mes in ["diciembre", "enero", "febrero"]:
    print("Estamos en Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Estamos en Primavera")
elif mes in ["junio", "julio", "agosto"]:
    print("Estamos en Verano")
elif mes in ["septiembre", "octubre", "noviembre"]:
    print("Estamos en Otoño")
else:
    print("Mes no válido")  