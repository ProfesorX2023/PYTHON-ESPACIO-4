from tabulate import tabulate

def calcular_interes_compuesto(principal, tasa_interes, tiempo, n):
    """
    Calcula el monto total acumulado con interés compuesto.

    Args:
    principal (float): Monto inicial del préstamo.
    tasa_interes (float): Tasa de interés anual (en decimal).
    tiempo (int): Tiempo en años.
    n (int): Número de veces que se capitaliza el interés por año.

    Returns:
    float: Monto final acumulado.
    """
    monto_final = principal * (1 + tasa_interes / n) ** (n * tiempo)
    return monto_final

def generar_resumen_deuda(principal, tasa_interes, tiempo_anios, n):
    """
    Genera un resumen de la deuda mes a mes.

    Args:
    principal (float): Monto inicial del préstamo.
    tasa_interes (float): Tasa de interés anual (en decimal).
    tiempo_anios (int): Tiempo del préstamo en años.
    n (int): Número de veces que se capitaliza el interés por año.
    """
    resumen = []
    deuda_actual = principal

    # Calcular mes a mes durante el tiempo del préstamo
    for mes in range(1, tiempo_anios * 12 + 1):
        interes_mensual = tasa_interes / n
        deuda_actual = deuda_actual * (1 + interes_mensual)
        resumen.append([mes, round(deuda_actual, 2)])

    # Mostrar tabla de resumen
    print(tabulate(resumen, headers=["Mes", "Deuda Acumulada"], tablefmt="grid"))

# Parámetros de ejemplo
principal = 5000  # Monto inicial del préstamo
tasa_interes = 0.05  # Tasa de interés anual (5%)
tiempo_anios = 2  # Tiempo del préstamo en años
n = 12  # Capitalización mensual

# Generar resumen de deuda
generar_resumen_deuda(principal, tasa_interes, tiempo_anios, n)
