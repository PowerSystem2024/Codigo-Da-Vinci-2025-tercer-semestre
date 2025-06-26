#AGREGAR ESTO A RequestHandler EN BACKEND.PY

def ver_pedidos(self, usuario_id):
    try:
        cursor.execute("""
            SELECT fecha, punto_retiro, productos, estado
            FROM pedidos
            WHERE usuario_id = %s
            ORDER BY fecha DESC
        """, (usuario_id,))
        resultados = cursor.fetchall()

        pedidos = [
            {
                'fecha': str(row[0]),
                'punto_retiro': row[1],
                'productos': row[2],
                'estado': row[3]
            }
            for row in resultados
        ]
        self.responder(200, {'pedidos': pedidos})
    except Exception as e:
        self.responder(500, {'message': f'Error al obtener pedidos: {str(e)}'})
