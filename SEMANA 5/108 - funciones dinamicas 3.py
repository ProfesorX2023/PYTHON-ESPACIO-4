def cantidad_pares(lista):
    contador = 0
    for n in lista:
        if n%2==0:
            contador += 1
        else:
            pass

    return contador

lista_numeros = [2,4,6,7,9,10,12,3,14]

print(cantidad_pares(lista_numeros))