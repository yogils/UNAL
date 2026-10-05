#Crear un programa para solicitar algunos valores importantes para una receta de cocia
#los valores que debe introducir el usuario son:
#Nombre de la redeta, ingredientes, tiempo de preparacion en minutos,dificultad(facil, media, alta)

print("RESETA DE COCINA PARA DISFRUTAR")

nombre_de_la_receta = input("Como se llama tu platillo?: ")
ingredientes = input("Cuales son los ingredientes de tu reeta: ")
tiempo = int(input("Cuanto tiempo tarda la coccion: "))
dificultad = input("Cual es la dificultad de la preparacion: ")

print(f"\nMi receta se llama: {nombre_de_la_receta}, \nLos ingredientes para la preparacion son los siguientes: {ingredientes}, \nEl tiempo de coccion es: {tiempo} Minutos, \nRealmente es muy: {dificultad}")