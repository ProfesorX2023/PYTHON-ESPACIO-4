class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    vivo = True

    def volar(self):
        print("El pajaro esta volando")


piolin = Pajaro(2, "Amarillo")

piolin.nacer()

print(piolin.color)
print(piolin.edad)

pajaro_loco = Pajaro(5, "Azul con Naranja")

print(pajaro_loco.color)

pajaro_loco.nacer()

piolin.volar()