from random import randint

intentos = 0
estimado = 0

numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado en un número entre 1 y 100 \nTienes 8 intentos para adivinar")

while intentos<8:
    intentos += 1
    print(f"Intento No. {intentos}")
    estimado = int(input("Introduce tu apuesta: "))
    if estimado == numero_secreto:
        print(f"Felicidades, acertaste el número secreto es {numero_secreto}")
        break
    elif estimado >100 or estimado <0:
        print(f"Número fuera de rango esto te costó un intento \nte quedan {8 - intentos}")
    elif estimado>numero_secreto:
        print(f"Has elegido uno mayor, intenta con algo menor \nNúmero errado te quedan {8 - intentos}")
    elif estimado<numero_secreto:
        print(f"Has elegido uno menor, intenta con algo mayor \nNúmero errado te quedan {8 - intentos}")



if estimado != numero_secreto:
    print(f"GAME OVER. El número secreto era: {numero_secreto}")
