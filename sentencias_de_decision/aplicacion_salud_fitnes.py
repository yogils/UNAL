#Aplicacion de salud y firnes
print("Bienvenido a la aplicacion de salud y fitness")  

n_usuario = input("Ingrese su nombre de usuario: ")
pasos_caminados_hoy = int(input("Ingrese los pasos que ha caminado hoy: "))

meta_pasos_diarios = 10000
calorias_por_paso = 0.04
calorias_diarias = pasos_caminados_hoy * calorias_por_paso

if pasos_caminados_hoy >= meta_pasos_diarios:
    print(f"¡Felicidades, {n_usuario}! Has alcanzado tu meta diaria de pasos.")
    print(f"Has quemado aproximadamente {calorias_diarias:.2f} calorías hoy.")
else:
    pasos_restantes = meta_pasos_diarios - pasos_caminados_hoy
    print(f"¡Ánimo, {n_usuario}! Te faltan {pasos_restantes} pasos para alcanzar tu meta diaria.")
    print(f"Has quemado aproximadamente {calorias_diarias:.2f} calorías hoy.")