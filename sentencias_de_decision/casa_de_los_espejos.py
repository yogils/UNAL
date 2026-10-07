#casa de los esperos del parque de diversiones
print("Bienvenido a la casa de los espejos")

edad = int(input("Cual es tu edad?: "))
tiene_miedo_a_la_oscuridad = input("La oscuridad te genera miedo? (Si/No): ").lower()
acompanante = input("Vas a ir acompañado? (Si/No): ").lower()

if edad >= 18 and tiene_miedo_a_la_oscuridad == "no" and acompanante == "si":
    print("¡Bienvenido a la casa de los espejos! Disfruta de la experiencia.")
elif edad >= 18 and tiene_miedo_a_la_oscuridad == "no" and acompanante == "no":
    print("Bienvenido a la casa de los espejos, espeo disfrutes de nuestra atraccion.")
elif edad >= 18 and tiene_miedo_a_la_oscuridad == "si"and acompanante == "no":  
    print("te recomiendo no entrar a la casa de los espejos, ya que la oscuridad te puede generar miedo.")
elif 13 <= edad < 18 and tiene_miedo_a_la_oscuridad == "no" and acompanante == "si":
    print("¡Bienvenido a la casa de los espejos! Disfruta de la experiencia.")
elif 13 <= edad < 18 and tiene_miedo_a_la_oscuridad == "si" and acompanante == "si":
    print("Bienvenido a la casa de los espejos, pero te recomiendo no quedarte solo ya que la oscuridad te puede generar miedo.")
elif 13 <= edad < 18 and tiene_miedo_a_la_oscuridad == "si" and acompanante == "no":    
    print("Lo siento, no puedes entrar a la casa de los espejos ya que la oscuridad te puede generar miedo y no tienes acompañante.")
elif edad < 13 and acompanante == "si":
    print("bienvenido a la casa de los espejos, pero te recomiendo no quedarte solo ya que la oscuridad te puede generar miedo.")
else:
    print("Lo siento, no puedes entrar a la casa de los espejos ya que eres menor de edad y no tienes acompañante.")