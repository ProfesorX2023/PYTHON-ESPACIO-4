def reducir_lista(lista_numeros):
    lista2 = list(set(lista_numeros))
    lista2.pop()
    return lista2

def promedio(lista2):
    return sum(lista2)/len(lista2)

lista_numeros =[1,2,15,7,2]

lista_reducida = reducir_lista(lista_numeros)
print(promedio(lista_reducida))