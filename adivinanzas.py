

import random


numero_secreto = random.randint(1,101)
adivinado = False
cant_intentos = 0
cant_maxintentos = 5

#while not adivinado:
#    numero = int(input("Introduce un numero del 1 al 100: ")) # TODO: convertir a numero con INT
#
#    if numero == numero_secreto:
#        print("¡Felicidades has adivinado el numero secreto!")
#        adivinado = True
#    elif numero < numero_secreto:
#        print("El numero es mayor al ingresado")
#    else:
#        print("El numero es menor al adivinado")

#while not adivinado and cant_intentos < cant_maxintentos:
#    numero = int(input("Introduce un numero del 1 al 100: "))
#    if numero == numero_secreto:
#        print("Felicidades adivinaste el numero secreto")
#    elif numero < numero_secreto:
#        print("El numero secreto es mayor al que elegiste")
#    else:
#        print("El numero secreto es menor al que elegiste")
#    
#    cant_intentos += 1 
#
#if not cant_intentos < cant_maxintentos:
#    print("Lo siento no tienes mas intentos")

print("Bienvenido al juego de adivinar el numero secreto!")

while not adivinado:
    if not cant_intentos < cant_maxintentos:
        print("Game Over")
        break
    
    numero = int(input("Elige un numero del 1 al 100: "))

    if numero == numero_secreto:
        print("Felicidades has adivinado el numero secreto")
    elif numero < numero_secreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
    cant_intentos +=1

print("SOS UN CHIMPANCE FELICITACIONES")