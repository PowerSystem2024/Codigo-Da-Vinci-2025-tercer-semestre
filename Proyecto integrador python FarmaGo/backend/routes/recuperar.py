from flask import Blueprint, request, jsonify
from controllers.auth_controller import recuperar_contraseña

recuperar_bp = Blueprint('recuperar', __name__)

@recuperar_bp.route('/recuperar', methods=['POST'])
def recuperar():
    data = request.json
    resultado = recuperar_contraseña(data)
    status_code = 200 if resultado.get('success') else 400
    return jsonify(resultado), status_code