def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus numeros es {sum(args)}"

print(numeros_persona("Pablo",1,2,3,4,5,6,7))