print(list(enumerate("Academia Fibonacci")))

lista_nombre = ["Marcos","Laura","Monica","Javier","Celina","Marta"]

print(list(enumerate(lista_nombre)))

for indice,nombre in enumerate(lista_nombre):
    print(f"{nombre} se encuentra en el indice: {indice}")

test_str = "python"
lista = list(test_str)
lista_indices = list(enumerate(lista))
for indice in lista_indices:
    print(indice[0])

lista_nombre = ["Marcos","Laura","Monica","Javier","Celina","Marta","Manolo","Juan"]
for indice,nombre in enumerate(lista_nombre):
    if nombre.upper().startswith('M'):
        print(indice,nombre)
    else:
        pass