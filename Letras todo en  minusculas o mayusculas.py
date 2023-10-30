#Solo minusculas

nombre=  str(input("Ingresa tu nombre:\n"))
texto=  str(input("Ingresa un pequeño texto:\n"))

#minusculas

print("\nValidando si todas las letras estan en MINUSCULAS=",nombre.islower())
print("\nResultado de todo minusculas=",nombre.lower())


print ("") #es solo para dar un espacio


#mayusculas

print("\nValidando si todas las letras estan en MAYUSCULAS=",nombre.isupper())
print("\nResultado de todo mayusculas=",nombre.upper())


print ("") #es solo para dar un espacio


#Todo lo que esta en MINUSCULAS se convertira en MAYUSCULAS y viseversa lo que esta en MAYUSCULAS pasara a MINUSCULAS 
print("\nDe minuscalas a mayusculas y viseversa")
print("\nResultado=",nombre.swapcase())


print ("") #es solo para dar un espacio


#Solo la primera letra estara en mayuscula, es mas para texto
print("\nSolo la primera letra sera en mayuscula ejemplo:")
print("\n",texto.capitalize())

print ("") #es solo para dar un espacio


#Centrar
print("\nSe centrara el texto ejemplo:")
print("\n",nombre.center(50))

print ("") #es solo para dar un espacio


#Centrar a la izquierda
print("\nSe centrara el texto a la izquierda ejemplo:")
print("\n",nombre.ljust(50))

#Centrar a la izquierda con caracter *
print("\nSe centrara el texto a la izquierda con caracter * ejemplo:")
print("\n",nombre.ljust(50,"*"))


print ("") #es solo para dar un espacio



#Centrar a la derecha
print("\nSe centrara el texto a la derecha ejemplo:")
print("\n",nombre.rjust(50))

#Centrar a la derecha con caracter *
print("\nSe centrara el texto a la derecha con caracter * ejemplo:")
print("\n",nombre.rjust(50,"*"))
