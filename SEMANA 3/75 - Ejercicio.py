"""
Tenemos un bar en un pais con las siguientes reglas
1. si es mayor de edad puede beber
2. si es mayor de 30 no puede entrar a una disco
3. los de 20 y 25 tienen entrada grátis
"""
edad = int(input("Ingresa tu edad"))
respuesta={True:"si",False:"no"}
print(f"1. Puede Beber? {respuesta[edad>=18]}")
print(f"2. Puede Entrar? {respuesta[edad>=18] and respuesta[edad<30]}")
print(f"3. Tiene Enrtada Grátis? {respuesta[edad==25] or respuesta[edad ==20]}")