control = True
lista = [2,4,6,8,2,1,3,4,6,8]
contador = 0
#en python un while se ejecuta si solo si se cumple la condicion
while(control): #funcionara si la condicion se cumple
    print(lista[contador])
    if lista[contador]%2 == 0:
        control = True
    else:
        control = False
    contador += 1