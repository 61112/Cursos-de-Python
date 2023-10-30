
dinero6= int (input("inserta dinero: \n"))

if dinero6>=48:
    print ("puedes recoger tu chocorrol.\n")
elif dinero6 <48:
    print("Te falta DINERO. Solo tienes 1 intentos mas\n")
    print("Ya que solo has insertado$",dinero6)

    deposito7=int(input("inserta mas dinero ultimo intento:\n"))
    dinero8=deposito7+dinero6
    print("$",dinero8)

    if dinero8>=48:
       print ("Puedes recoger tu chocorrol")

    elif dinero8 <48:
       print("lo siento no acumulaste el dinero suficiente. Que tengas buen dia\n")
