from flask import Blueprint, render_template
import sqlite3

detalle_producto_bp = Blueprint('detalle_producto', __name__)

@detalle_producto_bp.route('/producto/<int:producto_id>')
def ver_detalle_producto(producto_id):
    with sqlite3.connect("farmago.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, nombre, descripcion, precio, stock, imagen_url 
            FROM productos WHERE id = ?
        """, (producto_id,))
        producto = cursor.fetchone()

    if producto:
        producto_data = {
            "id": producto[0],
            "nombre": producto[1],
            "descripcion": producto[2],
            "precio": producto[3],
            "stock": producto[4],
            "imagen_url": producto[5]
        }
        return render_template('detalle_producto.html', producto=producto_data)
    else:
        return "Producto no encontrado", 404