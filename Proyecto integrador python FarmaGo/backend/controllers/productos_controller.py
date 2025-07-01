# controllers/productos_controller.py

import psycopg2
from database.connection import get_connection

def obtener_productos_por_categoria(categoria=None):
    conn = get_connection()
    cursor = conn.cursor()

    if categoria:
        cursor.execute("SELECT * FROM productos WHERE categoria = %s", (categoria,))
    else:
        cursor.execute("SELECT * FROM productos")

    productos = []
    for row in cursor.fetchall():
        productos.append({
            "id": row[0],
            "nombre": row[1],
            "descripcion": row[2],
            "precio": row[3],
            "categoria": row[4],
            "imagen_url": row[5]
        })

    cursor.close()
    conn.close()
    return productos