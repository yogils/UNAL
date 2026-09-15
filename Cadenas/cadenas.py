# ejemplos de cadenas en python
print("\ncadenas con comillas dobles ")
cadena = "Esto es una prueba de 'cadenas'en python"
print(cadena)
print("\ncadenas con comillas simples ")   
cadena2 = 'Esto es otra prueba de "cadenas" en python'
print(cadena2)

#cadenas con comillas triples o multilinea
print("\ncadenas con comillas triples o multilinea ")
menu = """
Menu del dia
--------------------
1. Hamburguesa
2. Pizza
3. Ensalada
4. Sopa
5. Postre
"""
print(menu)

print("\nprueba de correo electronico con comillas triples o multilinea ")
correo = """
Muy buenas tardes,
Le informamos que su pedido ha sido procesado correctamente y será enviado a la dirección indicada.
Gracias por su preferencia.
quedo muy atento a cualquier duda o comentario.
"""
print(correo)

#Error cuando en la misma linea se usasn comillas dobles dos veces la solucion es adicionar backslash (\) 
# antes de las comillas dobles que se quieren usar dentro de la cadena
print("\nError cuando en la misma linea se usan comillas dobles dos veces ")
cadena3 = "Esto es un error de \"cadenas\" en python"
print(cadena3)

print("\nejemplodos de cadenas con comillas dobles y simples ")
cadena4 = 'Esto es una prueba de \'cadenas\' en python'
print(cadena4)

#Tabulaciones y saltos de linea en cadenas
print("\nTabulaciones y saltos de linea en cadenas ")
cadena5 = "Esto es una prueba de \n\tcadenas en python"
print(cadena5)

print("\n1234123412341234123412341234123412341234")
cadena6="\tEsto es una prueba de \n\tcadenas en python"
print(cadena6)

#Imprimir \ deparando textos
print("\nImprimir \ separando textos ")
cadena7 = "Esto es una prueba de \\cadenas en python"
print(cadena7)  

print("\n")
cadena8 = "Esto\\es\\t\\u\\n\\a\\p\\r\\u\\e\\b\\a de \\cadenas en python"
print(cadena8)

#cadena cruda (raw string)r para que no se interpreten los caracteres especiales
print("\ncadena cruda (raw string) para que no se interpreten los caracteres especiales ")
cadena9 = r"Esto\ es\ una\ prueba \de \cadenas \en \python"
print(cadena9)

