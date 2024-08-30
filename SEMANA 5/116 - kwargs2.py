def lista_atributos(**kwargs):
    keyword = []
    for clave,valor in kwargs.items():
        keyword.append(valor)
    return keyword


print(lista_atributos(nombre="Luis",edad=6,Mayor=True,pais="Guatemala"))