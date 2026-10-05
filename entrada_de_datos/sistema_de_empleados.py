#vamos a crear un sistema de actualizacion de empleados
print("ESTE ES UN SISTEMA DE ACTUALIZACION DE DATOS DE UN EMPLEADO")

nombre_del_empleado = input("Ingresa el nombre del empleado: ") 
edad_del_empleado = int(input("Cual es la edad: "))
salario_del_empleado = float(input("Cuanto es el salario el empleado: "))
es_jefe_de_departamento = input("Es jefe de departamento (Si / No)?: ")
es_jefe_de_departamento = es_jefe_de_departamento.lower() == "Si"

print(f"Nombre del empleado: {nombre_del_empleado}, \nEdad del Empleado: {edad_del_empleado}, \nSalario del emplevalo es $: {salario_del_empleado},\nEs jefe de departament: {es_jefe_de_departamento}")