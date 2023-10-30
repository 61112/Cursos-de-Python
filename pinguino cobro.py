
dinero3= int (input("Inserta dinero: \n"))

if dinero3>=9: 
    print ("Puedes recoger tu Pinguino.\n")
elif dinero3 <9:
    print("Te falta dinero. Solo tienes 1 intentos mas\n")
    print("Ya que solo has insertado $",dinero3)

    deposito4=int(input("\nInserta mas dinero ultimo intento:\n"))
    dinero5=deposito4+dinero3
    print("Has insertado $",dinero5)

    if dinero5>=9:
       print ("\nPuedes recoger tu pinguino")

    elif dinero5 <9:
       print("\nLo siento no acumulaste el dinero suficiente. Que tengas buen dia.\n")
