from flask import Blueprint, request, jsonify
from controllers.auth_controller import registrar_usuario

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    resultado = registrar_usuario(data)
    return jsonify(resultado)