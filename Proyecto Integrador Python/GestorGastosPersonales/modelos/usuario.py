class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Usuario({self.id_usuario}): {self.nombre} - {self.correo}"

    @classmethod
    def desde_fila(cls, fila):
        return cls(fila[0], fila[1], fila[2])