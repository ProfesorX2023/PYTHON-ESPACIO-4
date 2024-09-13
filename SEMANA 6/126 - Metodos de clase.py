class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(cls.vivo)

maradona = Jugador()
print(maradona.vivo)
maradona.revivir()