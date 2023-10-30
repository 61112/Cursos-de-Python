#Imprimir titulo 1
titulo= "Rango en Numeros"
print(titulo.center(40,"="))

#************************************************

#   range ( start, stop, step)
#   Donde:

#  start= comienzo
#  stop= alto
#  step= incremento

n= range (10)

print(f"El rango es: {n}")

#************************************************
#Imprimir titulo 2
titulo= "for con rango"
print(titulo.center(40,"="))

#************************************************


#bucle for con rango


for indice in range(10):
    print(indice)
print("Fin del programa")

print("")
print("")









#************************************************
#Imprimir titulo 3
titulo= "Tabla de Multiplicar"
print(titulo.center(40,"="))

#************************************************


num= int(input("Ingresa el numero de la tabla quq deceas multiplicar:"))

for multiplica in range(11):
    print( f"{num} x {multiplica} = {num * multiplica}")

print("Fin del programa")






