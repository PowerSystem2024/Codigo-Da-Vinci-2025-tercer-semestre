from flask import Blueprint, request, jsonify
from controllers.auth_controller import iniciar_sesion

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    resultado = iniciar_sesion(data)
    status_code = 200 if resultado.get('success') else 401
    return jsonify(resultado), status_code