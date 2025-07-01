class Usuario:
    """
    Clase que representa un usuario del sistema.

    Atributos:
        id (int): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        correo (str): Correo electrónico único del usuario.
        contraseña (str): Contraseña hasheada del usuario. 
            NO almacenar la contraseña en texto plano.
    """

    def __init__(self, id=None, nombre=None, correo=None, contraseña=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña  # Debe ser la contraseña hasheada

    def __repr__(self):
        return f"<Usuario id={self.id} correo={self.correo}>"
    
class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock, imagen_url):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen_url = imagen_url

    def __repr__(self):
        return f"<Producto {self.nombre}>"   