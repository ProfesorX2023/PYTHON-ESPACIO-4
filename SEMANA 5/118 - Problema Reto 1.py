def devolver_distintos(num1, num2, num3):
    lista_suma = [num1,num2,num3]
    if sum(lista_suma) > 15:
        return max(lista_suma)
    elif sum(lista_suma) < 10:
        return min(lista_suma)
    else:
        if num1 != max(lista_suma) and num1 != min(lista_suma):
            return num1
        elif num2 != max(lista_suma) and num2 != min(lista_suma):
            return num2
        else:
            return num3



print(devolver_distintos(5,1,4))


