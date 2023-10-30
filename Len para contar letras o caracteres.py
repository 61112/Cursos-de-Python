#Funcion Len
#Sirve para contar los caracteres
titulo= "Len"
print(titulo.center(40,"="))

#Opcion 1
print("")
print("LALO tiene", len("LALO"),"caracteres")

#Opcion 2
print("")
longitud= len ("Hola Mundo")
print("La palabra Hola Mundo tiene", longitud,"caracteres, ya que el programa tambien cuenta los espacios")

print("")

#Funcion count
#Sirve para contar los caracteres

string= "Hola mundo"
contador= 0
titulo1= "Count"
print(titulo1.center(40,"="))

contador = string.count("H")
print(f"\n La letra H se encontro {contador} vez en la cadena: {string}")
contador = string.count("o")
print(f"\n La letra o se encontro {contador} veces en la cadena: {string}")
