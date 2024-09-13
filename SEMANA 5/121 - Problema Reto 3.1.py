def chequear_consectuvos(*args):
    for i in range(len(args)-1):
        if args[i] == 0 and args[i+1]==0:
            return True
    return False

def obtener_numeros():
    numeros = []
    print("Ingresa los números uno por uno. Presiona ENTER sin escribir nada para Terminar")
    while True:

        numero_usuario = input("Ingresa un número")

        if numero_usuario == "":
            break

        try:
            numeros.append(int(numero_usuario))
        except ValueError:
            print("Por favor, ingresa un número válido")

        resultado = chequear_consectuvos(*numeros)
        print(resultado)

obtener_numeros()