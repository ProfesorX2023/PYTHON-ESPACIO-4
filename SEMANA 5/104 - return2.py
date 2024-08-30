def usd_a_eur(monto):
    return monto*0.90

valor = int(input('Ingrese la cantidad en dorales'))
dolares = usd_a_eur(valor)

print(f"{valor} dolares son {dolares} euros")