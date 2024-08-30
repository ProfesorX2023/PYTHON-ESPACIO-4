def suma_absolutos(*args):
    total = 0
    for arg in args:
        total = abs(arg) + total
    return total

print(suma_absolutos(1,-1,-2,2,4,5,-9))