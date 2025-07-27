
from flask import Blueprint, jsonify
from controllers.puntos_controller import listar_puntos_retiro

puntos_retiro_bp = Blueprint('puntos_retiro', __name__)  # Cambié aquí

@puntos_retiro_bp.route('/puntos-retiro', methods=['GET'])
def puntos_retiro():
    puntos = listar_puntos_retiro()
    return jsonify(puntos)