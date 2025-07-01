# routes/productos.py

from flask import Blueprint, request, jsonify
from controllers.productos_controller import obtener_productos_por_categoria

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['GET'])
def listar_productos():
    categoria = request.args.get('categoria')
    productos = obtener_productos_por_categoria(categoria)
    return jsonify(productos)

