from datetime import datetime

class Gasto:
    def __init__(self, id_gasto, id_usuario, id_categoria, monto, descripcion, fecha=None):
        self.id_gasto = id_gasto
        self.id_usuario = id_usuario
        self.id_categoria = id_categoria
        self.monto = monto
        self.descripcion = descripcion
        self.fecha = fecha or datetime.now().strftime('%Y-%m-%d')

    def __str__(self):
        return (f"Gasto({self.id_gasto}): Usuario {self.id_usuario}, "
                f"Categoría {self.id_categoria}, Monto ${self.monto}, "
                f"Descripción: {self.descripcion}, Fecha: {self.fecha}")

    @classmethod
    def desde_fila(cls, fila):
        return cls(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])