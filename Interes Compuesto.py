import pandas as pd
from tabulate import tabulate

def calcular_interes_compuesto(principal, tasa_interes, tiempo, n):
    monto_final = principal * (1 + tasa_interes / n) ** (n * tiempo)
    return monto_final

def generar_tabla_resumen(datos, metodo='tabulate'):
    if metodo == 'tabulate':
        print(tabulate(datos, headers='keys', tablefmt='grid'))
    elif metodo == 'pandas':
        df = pd.DataFrame(datos)
        print(df.to_markdown())
    else:
        raise ValueError("Método no soportado. Use 'tabulate' o 'pandas'.")

# Ejemplo de uso
resultados = [
    {"Principal": 1000, "Tasa de Interés": 0.05, "Años": 5, "n": 12, "Monto Final": calcular_interes_compuesto(1000, 0.05, 5, 12)},
    {"Principal": 2000, "Tasa de Interés": 0.04, "Años": 10, "n": 4, "Monto Final": calcular_interes_compuesto(2000, 0.04, 10, 4)}
]

generar_tabla_resumen(resultados, metodo='tabulate')
