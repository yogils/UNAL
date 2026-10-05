#funcion bool

print("datos booleanos")
print(bool(0))
print(bool(0.0))
print(bool(-1))
print(bool(""))
print(bool("estoy nadando"))
print(bool("no"))
#Errores comunes

respuesta_usuario = "False"
es_verdad = bool(respuesta_usuario)
print(f"la respuesta real es: {es_verdad}")