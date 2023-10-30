string= input("Ingresa un texto pequeño:")

print("")
print(f"El texto que introdujo fue:{string}")
print("")

palabra= str(input("Ingresa la palabra que quieres eliminar:"))
print("")

substring=""

indice= string.find(palabra)

substring= string [0: indice] + string[indice + len(palabra) + 1 :]

print(f"CADENA RESULTANTE:{substring}")
