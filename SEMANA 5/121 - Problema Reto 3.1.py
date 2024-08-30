def check_consecutive_zeros(*args):
    # Recorremos la lista de argumentos para verificar ceros consecutivos
    for i in range(len(args) - 1):
        # Comprobamos si el elemento actual y el siguiente son ceros
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False


def get_numbers():
    numbers = []  # Lista para almacenar los números ingresados por el usuario
    print("Ingresa los números uno por uno. Presiona ENTER sin escribir nada para terminar.")
    while True:
        # Solicitamos un número al usuario
        user_input = input("Ingresa un número: ")

        # Verificamos si la entrada está vacía para terminar el ciclo
        if user_input == "":
            break

        try:
            # Convertimos la entrada a un entero y la agregamos a la lista
            numbers.append(int(user_input))
        except ValueError:
            # En caso de error en la conversión, informamos al usuario
            print("Por favor, ingresa un número válido.")

    # Convertimos la lista en una tupla y la pasamos a la función check_consecutive_zeros
    result = check_consecutive_zeros(*numbers)
    print(result)


# Llamamos a la función para iniciar el proceso
get_numbers()