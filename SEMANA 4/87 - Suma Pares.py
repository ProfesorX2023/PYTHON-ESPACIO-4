lista_numeros = [1,2,3,4,5,3,4,5,3,1,2,3,4,5,6,2,3,4,5,6,7,7]
par = 0
impar = 0
for numero in lista_numeros:
    if numero %2 == 0:
        par += numero
    else:
        impar += numero

print(f"La suma de los numeros pares es {par} \nLa suma de los impares es {impar}")


