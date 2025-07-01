from flask import Blueprint, request, jsonify, session

carrito_bp = Blueprint('carrito', __name__)

# Para este ejemplo simple usaremos session para guardar carrito por usuario (si querés DB, me decís)

@carrito_bp.route('/carrito/agregar', methods=['POST'])
def agregar_al_carrito():
    producto = request.json
    producto_id = producto.get('producto_id')
    cantidad = producto.get('cantidad', 1)

    if not producto_id:
        return jsonify({"success": False, "message": "Falta producto_id"}), 400

    carrito = session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)] += cantidad
    else:
        carrito[str(producto_id)] = cantidad

    session['carrito'] = carrito
    return jsonify({"success": True, "message": "Producto agregado al carrito", "carrito": carrito})

@carrito_bp.route('/carrito', methods=['GET'])
def ver_carrito():
    carrito = session.get('carrito', {})
    return jsonify({"carrito": carrito})

from flask import Blueprint, session, jsonify
from controllers.carrito_controller import obtener_detalle_carrito
from models.producto import get_productos_dict  # función que trae los productos como diccionario

carrito_bp = Blueprint('carrito', __name__)

@carrito_bp.route('/carrito', methods=['GET'])
def ver_carrito():
    carrito = session.get('carrito', {})
    productos_db = get_productos_dict()
    detalle, total = obtener_detalle_carrito(carrito, productos_db)
    
    return jsonify({
        'items': detalle,
        'total': total
    })