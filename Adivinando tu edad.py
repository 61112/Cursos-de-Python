nombre=  str(input("Ingresa tu nombre:\n"))
nacimiento= int(input("Ingresa el año en que naciste:\n"))
edad= 2023 - nacimiento
edad_promedio= 80 - edad
print("Hola {} actualmente tienes {} años\n".format(nombre,edad))
print("Por lo tanto {} solo te quedan {} años de vida aproximadamente\n".format(nombre,edad_promedio))
