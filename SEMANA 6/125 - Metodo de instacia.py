class Personaje:
    nombre = "Hanz"

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flechas(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        return self.cantidad_flechas
    
hanz = Personaje(10)

print(f"{hanz.nombre} ha lanzado 1 flecha le quedan {hanz.lanzar_flechas()} flechas")
print(f"{hanz.nombre} ha lanzado 1 flecha le quedan {hanz.lanzar_flechas()} flechas")
print(f"{hanz.nombre} ha lanzado 1 flecha le quedan {hanz.lanzar_flechas()} flechas")
print(f"{hanz.nombre} ha lanzado 1 flecha le quedan {hanz.lanzar_flechas()} flechas")
print(f"{hanz.nombre} ha lanzado 1 flecha le quedan {hanz.lanzar_flechas()} flechas")
