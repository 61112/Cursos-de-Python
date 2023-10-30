dinero= int (input("Inserta dinero: \n"))

if dinero>=18:
    print ("Puedes recoger tu producto\n")
elif dinero <18:
    print("Te falta dinero. Solo tienes 1 intentos mas\n")
    print("Ya que solo has insertado $",dinero)

    deposito1=int(input("\nIserta mas DINERO:\n"))
    dinero2=deposito1+dinero
    print("Has insertado $",dinero2)

    if dinero2>=18:
       print ("\nPuedes recoger tu producto\n")

    elif dinero2 <18:
       print("\nLo siento no a cumulaste el dinero suficiente. Que tengas buen dia\n")

       


