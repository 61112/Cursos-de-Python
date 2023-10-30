nombre=  str(input("Ingresa tu nombre:"))

print ("")

print (f"Bienvenido: {nombre} \n") #es para imprimir un comentario
print ("El Menu es:\n")

print ("1   Gancito       $18")
print ("2   Pinguinos     $9")
print ("3   Chocorroles   $48\n")


n= int (input("Escoje la operacion solo numero: \n"))




#operacion 1 - GANCITO

#NOTA: Es importante respetar los espacios en el if, print, if, elif.  Ya que de no ser asi "PYTHON" pensara que forma parte de otra condicion de IF
#NO BORRES NINGUN ESPACIO, SINO NO FUNCIONA

if n == 1 :
    print(f"{nombre} has escojido un gancito por favor ingresa  $18; No da cambio.\n")

    dinero= int (input(f"{nombre} inserta dinero: \n"))

if dinero>=18:
    print (f"{nombre} puedes recoger tu Gancito.\n")
elif dinero <18:
    print(f"{nombre} Te falta DINERO. Solo tienes 1 intentos mas\n")
    print("Ya que solo has insertado$",dinero)

    deposito1=int(input(f"{nombre} inserta mas dinero ultimo intento:\n"))
    dinero2=deposito1+dinero
    print("$",dinero2)

    if dinero2>=18:
       print (f"{nombre} Puedes recoger tu Gancito")

    elif dinero2 <18:
       print(f"{nombre} lo siento no acumulaste el dinero suficiente. Que tengas buen dia\n")




#operacion 2 - PINGUINOS

       if n == 2 :
         print(f"{nombre} has escojido un gancito por favor ingresa  $18; No da cambio.\n")

         dinero3 = int (input(f"{nombre} inserta dinero: \n"))
 
       if dinero3 >= 9:
    
         print (f"{nombre} puedes recoger tu Gancito.\n")
       elif dinero3<9:
         print(f"{nombre} Te falta DINERO. Solo tienes 1 intentos mas\n")
         print("Ya que solo has insertado$",dinero)

         deposito3=int(input(f"{nombre} inserta mas dinero ultimo intento:\n"))
dinero10=deposito3+dinero
print("$",dinero2)

if dinero3>=9:
 print (f"{nombre} Puedes recoger tu Gancito")

elif dinero3 <9:
 print(f"{nombre} lo siento no acumulaste el dinero suficiente. Que tengas buen dia\n")
 
     

#operacion 3 - CHOCORROLES

elif n == 3 :

      print(f"{nombre} has escojido unos chocorroles por favor ingresa  $48; No da cambio\n")

      opc3= int(input("INSERTA TU DINERO:\n"))

      if opc3 >= 48:
        print("Gracias puede recoger su producto\n")

      elif opc3 < 48:
        print (f"{nombre} Te falta dinero \n")


else:

      print("No seleccionaste ninguna opcion valida, Gracias por visitarnos")



