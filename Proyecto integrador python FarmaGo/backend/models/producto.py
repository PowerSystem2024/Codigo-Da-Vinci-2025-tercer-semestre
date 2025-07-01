class Producto:
    def __init__(self, id, nombre, descripcion, precio, categoria, imagen_url):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.imagen_url = imagen_url

    def __repr__(self):
        return f"<Producto {self.nombre} - {self.categoria}>"
    
import sqlite3

def get_productos_dict():
    conn = sqlite3.connect('farmago.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, precio FROM productos")
    productos = cursor.fetchall()
    conn.close()

    return {id: {'nombre': nombre, 'precio': precio} for i