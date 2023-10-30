print("La suma usando Acumulador")
print("")
print("Digita 5 numeros")
print("")
suma = 0;

for var in range(1,6):

	num = int(input("Igresa un número para sumar:"))

	if num >= 0:
		suma = suma + num

		print("")
print("La suma de los números es ",suma)
print("")
