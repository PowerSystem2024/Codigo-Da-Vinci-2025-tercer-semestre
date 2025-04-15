#1.6 Creación de clases de Exception personalizadas
class NumerosIgualesException (Exception): # extiende de la clase
    def __init__(self, mensaje):
        self.message = mensaje
        super().__init__(self.message) # Llamamos al constructor de la clase base