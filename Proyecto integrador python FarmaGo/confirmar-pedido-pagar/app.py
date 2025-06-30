from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

pedido_simulado = {
    "productos": [
        {"nombre": "Ibuprofeno 600mg", "cantidad": 2, "total": 4000},
        {"nombre": "Paracetamol", "cantidad": 1, "total": 1500}
    ],
    "total": 5500
}

def crear_base_datos():
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
        conn.commit()

@app.route('/')
def home():
    return redirect(url_for('confirmar_pedido'))

@app.route('/confirmar-pedido', methods=['GET', 'POST'])
def confirmar_pedido():
    if request.method == 'POST':
        productos = request.form.get('productos', '')  # el name debe coincidir con el input
        total = request.form.get('total', '')
        metodo_pago = request.form.get('metodo_pago', '')
        numero_tarjeta = request.form.get('numero_tarjeta', '')
        vencimiento = request.form.get('vencimiento', '')
        cvv = request.form.get('cvv', '')

        # Guardar en base de datos
        with sqlite3.connect("farmago.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pedidos (productos, total, metodo_pago, numero_tarjeta, vencimiento, cvv)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (productos, total, metodo_pago, numero_tarjeta, vencimiento, cvv))
            conn.commit()

        return redirect(url_for('pedido_exitoso'))

    return render_template('confirmar_pedido.html', pedido=pedido_simulado)

@app.route('/pedido-exitoso')
def pedido_exitoso():
    return render_template("pedido_exitoso.html")

if __name__ == '__main__':
    crear_base_datos()
    app.run(debug=True)
