class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja")

class Madre():
    def trabajar(self):
        print("Trabaja en la fiscalia")



class Hija(Madre, Padre):
    def jugar(self):
        print("La niña está jugando")


carmen = Hija()

carmen.trabajar()
carmen.reir()

jorge = Padre()

jorge.trabajar()
carmen.jugar()