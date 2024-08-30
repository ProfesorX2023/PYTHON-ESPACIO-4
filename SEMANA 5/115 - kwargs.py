def cantidad_atributos(**kwargs):
    contar = 0
    for clave, valor in kwargs.items():
        contar = contar + 1

    return contar



print(cantidad_atributos(nombre="Luis",edad=6,Mayor=True))