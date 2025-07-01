from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

pedido_bp = Blueprint('pedido', __name__)

# Simulación de pedido para mostrar en pantalla
pedido_simulado = {
    "productos": [
        {"nombre": "Ibuprofeno 600mg", "cantidad": 2, "total": 4000},
        {"nombre": "Paracetamol", "cantidad": 1, "total": 1500}
    ],
    "total": 5500
}

@pedido_bp.route('/')
def home():
    return redirect(url_for('pedido.confirmar_pedido'))

@pedido_bp.route('/confirmar-pedido', methods=['GET', 'POST'])
def confirmar_pedido():
    if request.method == 'POST':
        productos = request.form.get('productos', '')  # El name debe coincidir con el input del formulario
        total = request.form.get('total', '')
        metodo_pago = request.form.get('metodo_pago', '')
        numero_tarjeta = request.form.get('numero_tarjeta', '')
        vencimiento = request.form.get('vencimiento', '')
        cvv = request.form.get('cvv', '')

        # Guardar el pedido en la base de datos
        with sqlite3.connect("farmago.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    productos TEXT,
                    total REAL,
                    metodo_pago TEXT,
                    numero_tarjeta TEXT,
                    vencimiento TEXT,
                    cvv TEXT,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            cursor.execute('''
                INSERT INTO pedidos (productos, total, metodo_pago, numero_tarjeta, vencimiento, cvv)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (productos, total, metodo_pago, numero_tarjeta, vencimiento, cvv))
            conn.commit()

        return redirect(url_for('pedido.pedido_exitoso'))

    return render_template('confirmar_pedido.html', pedido=pedido_simulado)

@pedido_bp.route('/pedido-exitoso')
def pedido_exitoso():
    return render_template("pedido_exitoso.html")

from flask import Blueprint, request, jsonify
from controllers.pedido_controller import confirmar_pedido

pedidos_bp = Blueprint('pedidos', __name__)

@pedidos_bp.route('/confirmar-pedido', methods=['POST'])
def confirmar():
    data = request.json
    respuesta, estado = confirmar_pedido(data)
    return jsonify(respuesta), estado

@pedidos_bp.route('/mis-pedidos', methods=['GET'])
def ver_pedidos():
    usuario_id = request.args.get('usuario_id', type=int)

    respuesta, estado = listar_pedidos(usuario_id)
    return jsonify(respuesta), estado