from database.connection import get_connection

def obtener_puntos_retiro():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, direccion, ciudad, provincia 
        FROM puntos_retiro WHERE activo = TRUE
    """)
    resultados = cursor.fetchall()
    conn.close()

    puntos = [
        {
            "id": row[0],
            "nombre": row[1],
            "direccion": row[2],
            "ciudad": row[3],
            "provincia": row[4]
        } for row in resultados
    ]
    return puntos