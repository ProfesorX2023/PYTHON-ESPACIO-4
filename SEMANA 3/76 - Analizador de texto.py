texto = input("Ingresa un texto a tu elección: ")
letras = []

texto.lower()

letras.append(input("Ingresa la primera letra").lower())
letras.append(input("Ingresa la segunda letra").lower())
letras.append(input("Ingresa la tercera letra").lower())

print(letras)

'''
No puedes separar la paz de la libertad, porque nadie puede estar en paz, a no ser  que tenga su libertad
'''

#Busqueda de letas

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}', repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}', repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}', repetida {cantidad_letras3} veces")

# Cantidad de palabras
print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

# Buscar letra de inicio y de fin
print("LETRA DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_final}")

# Texto Invertido
print("TEXTO INVERTIDO")
palabras.reverse()
print(palabras)
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés vá a decir: \n {texto_invertido}")

# Buscando la palabra Python
print("\n")
print("BUSCANDO LA PALABRA PYTHON")
palabra = input("Ingresa una palabra para buscar")
buscar_palabra = palabra in texto
dic={True:'si',False:'no'}
print(f"La palabra {palabra} {dic[buscar_palabra]} aparece en el texto")
