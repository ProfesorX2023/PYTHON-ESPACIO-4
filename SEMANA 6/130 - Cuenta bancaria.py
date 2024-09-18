

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: Q.{self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Depósito Aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro Aceptado")
        else:
            print("No tienes disponibilidad")


def crear_cliente():
    nombre_cl = input("Ingrese su nombre:")
    apellido_cl = input("Ingrese su apellido")
    numero_cuenta = input("Ingrese su número de cuenta:")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = ''
    while opcion != 'S':
        print('Elige: Depositar(D), Retirar(R), o Salir(S)')
        opcion = input().upper()
        if opcion == 'D':
            monto_dep = int(input("Ingresa el monto a Depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Ingrese el monto a Retirar: "))
            mi_cliente.retirar(monto_ret)

        print(mi_cliente)

        print("Gracias por utilizar el banco Python")


inicio()