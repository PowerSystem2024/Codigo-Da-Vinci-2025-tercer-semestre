import sqlite3

def guardar_pedido(usuario_id, productos_json, total, metodo_pago):
    conn = sqlite3.connect("farmago.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pedidos (usuario_id, productos, total, metodo_pago)
        VALUES (?, ?, ?, ?)
    """, (usuario_id, productos_json, total, metodo_pago))

    conn.commit()
    conn.close()

import sqlite3

def obtener_pedidos_por_usuario(usuario_id):
    conn = sqlite3.connect("farmago.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT fecha, productos, metodo_pago, total
        FROM pedidos
        WHERE usuario_id = ?
        ORDER BY fecha DESC
    """, (usuario_id,))

    resultados = cursor.fetchall()
    conn.close()

    pedidos = []
    for row in resultados:
        pedidos.append({
            "fecha": row[0],
            "productos": row[1],
            "metodo_pago": row[2],
            "total": row[3]
        })

    return pedidos

def obtener_pedidos_por_usuario(usuario_id):
    conn = sqlite3.connect("farmago.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT fecha, productos, metodo_pago, total, estado
        FROM pedidos
        WHERE usuario_id = ?
        ORDER BY fecha DESC
    """, (usuario_id,))

    resultados = cursor.fetchall()
    conn.close()

    pedidos = []
    for row in resultados:
        pedidos.append({
            "fecha": row[0],
            "productos": row[1],
            "metodo_pago": row[2],
            "total": row[3],
            "estado": row[4]
        })

    return pedidos
