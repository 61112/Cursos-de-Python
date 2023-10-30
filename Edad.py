nombre=  str(input("Ingresa tu nombre:"))

print ("")

print (f"Bienvenido: {nombre} ") #es para imprimir un comentario

print ("")

n= int(input("Ingresa tu edad SOLO NUMEROS ENTEROS:"))


print ("")


if n > 18:
    print(f"{n} es mayor que 18; Si Te Podemos Vender")

elif n == 18 :
      print(f"{n} es igual que 18; Si Te Podemos Vender")

else:

      print(f"{n} es menor que 18; NO Te Podemos Vender")

