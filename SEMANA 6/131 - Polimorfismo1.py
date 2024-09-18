class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzar flechas")

class Samurai():
    def atacar(self):
        print("Ataque con Katana")

musashi = Samurai()
lowe = Mago()
hanz = Arquero()

personajes = [hanz, lowe, musashi]

for personaje in personajes:
    personaje.atacar()