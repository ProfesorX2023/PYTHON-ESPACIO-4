class Personaje:
    real = False

    def __init__(self, especie, magico, poder):
        self.especie = especie
        self.magico = magico
        self.poder = poder

max = Personaje("Humano",False,"Espadachin")
ken = Personaje("Centauro",False,"Lancero")
tao = Personaje("Elfo",True,"Lanzador de conujros")

print(f"Max es un {max.poder}, es real? {max.real}, es mágico? {max.magico}, es especie {max.especie} ")
print(f"Ken es un {ken.poder}, es real? {ken.real}, es mágico? {ken.magico}, es especie {ken.especie} ")
print(f"tao es un {tao.poder}, es real? {tao.real}, es mágico? {tao.magico}, es especie {tao.especie} ")
