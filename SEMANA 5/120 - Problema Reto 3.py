"""flag = 1
lista = []
contadorCeros = 0
while(flag !=0):
    num = int(input("Ingrese un número"))
    lista.append(num)
    if num == 0 and contadorCeros >=1:
        break
    elif num!=0:
        contadorCeros=0
    else:
        contadorCeros+=1


print(lista)"""

"""def suma(*args):
    return sum(args)

print(suma(1,2,5,6,4))"""

def contarCeros(*args):
    x = 0
    for n in args:
        if x+1 == len(args):
            return False
        elif args[x] == 0 and args[x+1] == 0:
            return True
        else:
            pass

        x+=1

    return False

print(contarCeros(5,6,1,0,9,3,5,0,0))


