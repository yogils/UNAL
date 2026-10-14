#ahora vamos con listas
print("Manejo de listas.")

mi_lista = [1, 2, 3, 4, 5]

print(f"Esta es la original -> {mi_lista}")
print(f"El largo de la lista es -> {len(mi_lista)}")
#Acceder a los elementos 
print((f"\nahora vammos a accder a un elemento dentro de la lista: {mi_lista[4]}"))
#modificar listas 
mi_lista[1] = 23
print(f"Asi queda mi nueva lista -> {mi_lista} con cantidad de {len(mi_lista)} caracteres.")
#Agregar elementos a mi lista 
mi_lista.append(7)
print(f"Esta es mi nueva lista -> {mi_lista} con cantidad de {len(mi_lista)} caracteres.")
#Anadir un elemento en el un indice especifico
mi_lista.insert(2, 15)
print(f"Esta es mi nueva lista -> {mi_lista} con una cantidad de {len(mi_lista)} caracteres.")
#Eliminar elementos de una lita
mi_lista.remove(23)
mi_lista.insert(1, 2)
print(f"Esta es mi nueva lista -> {mi_lista} con una cantidad de {len(mi_lista)} caracteres")
#obtener una sublista de una lista
sublista = mi_lista[1 : 3]
print(f"Esta es mu sublista -> {sublista}")