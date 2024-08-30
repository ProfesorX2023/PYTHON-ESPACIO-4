def potencia(base,exponente):
    resultado = base**exponente
    return resultado

base=int(input("Ingrese la base"))
exponente=int(input("Ingrese el exponente"))

valorPotencia = potencia(base,exponente)

print(f"El valor de la potencia es: {valorPotencia}")