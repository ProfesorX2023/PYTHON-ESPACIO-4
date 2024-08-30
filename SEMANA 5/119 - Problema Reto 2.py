palabra = 'Entretenido'

def ordenar(cascaRabias):
    lista = list(palabra.lower())
    lista.sort()
    let = " "
    lista2=[]
    for letra in lista:
        if let != letra:
            lista2.append(let)
            let = letra
    lista2.remove(" ")
    return lista2

print(ordenar(palabra))