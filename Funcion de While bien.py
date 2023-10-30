numero = 19

intento = 0

max_intentos = 3

while intento < max_intentos:
    
    number = int(input("Adivina el numero: "))
    
    intento += 1
    
    if number == numero:
        
        print("Enhorabuena adivinaste el numero")
        
        break
    
    
        print("Has fallado vuelve a intentarlo")
else:
    print("No tienes mas oportunidades")
