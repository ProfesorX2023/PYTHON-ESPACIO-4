from random import choice

#Funcion para elegir la palabra al azar
def palabra_al_azar():
    palabras = ['chile','calabaza','vestido','sandalias','responsabilidad','municipalidad','panaderia','guatemala']
    return choice(palabras)

#Funcion para convertir la palabra a guiones
def convertir_guiones(palabra_secreta):
    guiones = []
    for n in palabra_secreta:
        guiones.append("_")
    return guiones

#Funcion para verficar si se ingresa una letra
def verificar():
    letra = "%"
    while letra not in "abcdefghijklmnñopqrstuvwxyz":
        letra = input("Ingrese una letra")

    return letra

#comienzo del juego

palabra_secreta = list(palabra_al_azar())
guiones = convertir_guiones(palabra_secreta)
lista_incorrectas = []
vidas = 7

print("Bienvenido al juego del ahorcado")
print("El juego trata de que adivines las palabras")
print("Puedes escribir una letra para darte una pista")
print("El juego te dirá en donde aparece la letra para reducir la palabra")
print("Tienes 7 vidas")
print(guiones)

while True:
    intento = verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n] = intento
                print(guiones)

        if guiones == palabra_secreta:
            print("Felicidades adivinaste")
            palabra = "".join(palabra_secreta)
            print(f"La palabra es {palabra}")

    else:
        lista_incorrectas.append(intento)
        print("Lista de intentos incorrectos")
        print(lista_incorrectas)
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
        if vidas == 0:
            print("GAME OVER")
            palabra = "".join(palabra_secreta)
            print(f"La palabra secreta era {palabra}")
            break
