import sqlite3

def obtener_puntos_retiro():
    conn = sqlite3.connect('farmago.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, direccion, ciudad, provincia 
        FROM puntos_retiro WHERE activo = 1
    """)
    puntos = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "nombre": row[1],
            "direccion": row[2],
            "ciudad": row[3],
            "provincia": row[4]
        }
        for row in puntos
    ]

from flask import Blueprint, jsonify
from controllers.puntos_controller import listar_puntos_retiro

puntos_bp = Blueprint('puntos', __name__)

@puntos_bp.route('/puntos-retiro', methods=['GET'])
def puntos_retiro():
    puntos = listar_puntos_retiro()
    return jsonify(puntos)