class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self):
        return f"Categoría({self.id_categoria}): {self.nombre}"

    @classmethod
    def desde_fila(cls, fila):
        return cls(fila[0], fila[1])