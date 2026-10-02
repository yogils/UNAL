#remplazar cadenas en python
print("vamos a prender a remplazar cadenas en python")
r_subcadena = "Hola a todos ; Hola a todos soy yo soy yo"
nuevo = r_subcadena.replace("Hola a todos", "espero esten bien" , 2)

print(r_subcadena)
print(nuevo)


mensaje = """Quiero tomarme un momento para decirte algo que muchas veces no sabemos cómo expresar con palabras. Hay personas que llegan a nuestra vida de una manera inesperada y, poco a poco, terminan ocupando un lugar muy especial en nuestro corazón. Tú eres una de esas personas.

Quiero que sepas que valoro muchísimo cada momento compartido, cada conversación, cada risa, cada consejo y hasta esos pequeños detalles que quizás para ti parecen insignificantes, pero que para mí tienen un significado enorme. A veces uno no se da cuenta de lo importante que puede llegar a ser alguien hasta que empieza a notar cuánto cambia su día simplemente por saber que esa persona está ahí.

La vida no siempre es fácil. Todos tenemos días buenos y días difíciles, momentos en los que sentimos que todo está saliendo bien y otros en los que simplemente necesitamos un poco de tranquilidad, compañía o alguien que nos recuerde que no estamos solos. Y por eso quiero agradecerte por estar, por ser tú, por tu manera de ser y por todo aquello que, consciente o inconscientemente, has aportado a mi vida.

No quiero que pienses que tienes que ser perfecto o que siempre tienes que estar bien. Todos tenemos errores, preocupaciones, inseguridades y momentos en los que no sabemos qué hacer. Lo importante es seguir adelante, aprender, levantarnos cuando caemos y valorar a las personas que realmente están a nuestro lado.

También quiero decirte que deseo de corazón que te vaya bien en todo lo que te propongas. Que puedas cumplir tus sueños, alcanzar tus metas y encontrar muchas razones para sonreír. Ojalá nunca pierdas esa esencia que te hace especial y que siempre encuentres personas que sepan valorar lo que eres y todo lo bueno que llevas dentro.

Si alguna vez dudas de ti, recuerda que tienes más valor del que imaginas. Si alguna vez sientes que no puedes, recuerda todo lo que ya has superado. Y si algún día las cosas no salen como esperabas, no significa que hayas fracasado; simplemente significa que todavía estás escribiendo tu historia.

No sé qué nos depare el futuro ni cuánto puedan cambiar las circunstancias, pero sí sé que hay personas que dejan huellas que no se borran fácilmente. Tú has dejado una de esas huellas en mi vida, y por eso quería decírtelo.

Gracias por cada instante, por cada palabra, por cada sonrisa y por cada recuerdo. Gracias simplemente por existir y por haber coincidido conmigo en este camino. Espero que la vida te devuelva multiplicado todo lo bueno que das y que nunca te falten motivos para seguir creyendo en ti.

Y si alguna vez necesitas recordar que alguien te aprecia, que alguien cree en ti y que alguien desea sinceramente que seas feliz, recuerda estas palabras. No tienes que responder nada especial. Solo quería que lo supieras, porque hay cosas que sentimos y que a veces dejamos pasar demasiado tiempo sin decirlas.

Te deseo lo mejor, hoy, mañana y siempre. Y pase lo que pase, espero que nunca olvides lo mucho que vales y lo importante que puedes llegar a ser para quienes tienen la fortuna de conocerte.

"""
nuevo1 = mensaje.replace("Todos tenemos días buenos y días difíciles","YO VIVO DE LAS FANTASIAS")
print(mensaje)
print(nuevo1)


