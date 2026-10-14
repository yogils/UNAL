#Vamos a crear un playlist 
#Vamos a crear un programa para administrar una lista de canciones
#debemos solicitar al usuario cuantas canciones desea agregar a la lista y posteriormente ir silocotando
#cada cancion que desea agregar a la lista
#seguidamente debe desplegar la lista de canciones en orden alfabetico
print("mi lista de reproduccion musical".upper())

lista_reproduccion = []
n_canciones = int(input("Cuantas canciones deseas agregar? "))
for indice in range(n_canciones):
    cancion = input(f"indique la cancion que desea agregar {indice + 1}: ")
    lista_reproduccion.append(cancion)


"""lista_reproduccion.append("Tusa - Karol G & Nicki Minaj")
lista_reproduccion.append("ADIVINO – Myke Towers & Bad Bunny")
lista_reproduccion.append("Chica Ideal – Sebastián Yatra & Guaynaa")
lista_reproduccion.append("Oye mi amor – Maná")
lista_reproduccion.append("Saturno – Pablo Alborán")
lista_reproduccion.append("Amapolas – Leo Rizzi")
lista_reproduccion.append("La Vida Es Un Carnaval – Celia Cruz")
lista_reproduccion.append("Adiós Amor – Christian Nodal")"""
lista_reproduccion.sort()

for cancion in lista_reproduccion:
    print(f"\n{cancion}")