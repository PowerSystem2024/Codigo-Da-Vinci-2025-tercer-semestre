import json
from models.pedido import guardar_pedido

def confirmar_pedido(data):
    usuario_id = data.get('usuario_id')
    productos = data.get('productos')  # Lista de productos
    total = data.get('total')
    metodo_pago = data.get('metodo_pago')

    if not usuario_id or not productos or not metodo_pago:
        return {"success": False, "message": "Faltan datos"}, 400

    productos_json = json.dumps(productos)
    guardar_pedido(usuario_id, productos_json, total, metodo_pago)

    return {"success": True, "message": "Pedido confirmado con éxito"}, 201

from models.pedido import obtener_pedidos_por_usuario

def listar_pedidos(usuario_id):
    if not usuario_id:
        return {"success": False, "message": "ID de usuario faltante"}, 400

    pedidos = obtener_pedidos_por_usuario(usuario_id)
    return {"success": True, "pedidos": pedidos}, 200