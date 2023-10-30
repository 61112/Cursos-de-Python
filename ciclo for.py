titulo= "IMPRIME LETRA POR LETRA"
print(titulo.center(40,"="))

string= input("Ingresa una palabra:")

for character in string:
    print(character)

print("Fin del programa")


titulo= "IMPRIME LAS LETRAS ALRREVEZ"
print(titulo.center(40,"="))

string= input("Ingresa una palabra:")
string_reversa= ""

for character in string:
    string_reversa= character + string_reversa

print(string_reversa)




