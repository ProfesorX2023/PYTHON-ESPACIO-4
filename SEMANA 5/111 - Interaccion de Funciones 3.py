from random import choice

lista_numeros = [1,2,3,4,5,6]

def lanzar_moneda():
    moneda = ["cara","escudo"]
    return choice(moneda)

moneda= lanzar_moneda()

def probar_suerte(moneda,lista_numeros):
    if moneda == "cara":
        lista_numeros = []
        return f"La lista se autodestruira "
    elif moneda == "escudo":
        return f"La lista se salvó {lista_numeros}"

print(probar_suerte(moneda,lista_numeros))