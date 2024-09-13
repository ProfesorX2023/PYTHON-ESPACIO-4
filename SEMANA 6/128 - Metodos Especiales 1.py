class Libro:


    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __len__(self):
        return self.paginas

    def __str__(self):
        return f"Libro: {self.titulo}, autor: {self.autor}"


libro1 = Libro("Cementerio de mascotas","Stephen King",1800)


print(str(libro1))
print(len(libro1))