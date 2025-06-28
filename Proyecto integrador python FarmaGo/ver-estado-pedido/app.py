from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home_redirect():
    return redirect('/mis-pedidos')

@app.route('/agregar-pedido')
def agregar_pedido():
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedidos (producto, total, estado) VALUES (?, ?, ?)",
                   ("Paracetamol 500mg", 2500, "En preparación"))
    conn.commit()
    conn.close()
    return redirect('/mis-pedidos')

@app.route('/cancelar-pedido/<int:pedido_id>')
def cancelar_pedido(pedido_id):
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id,))
    conn.commit()
    conn.close()
    return redirect('/mis-pedidos')

@app.route('/cambiar-estado/<int:pedido_id>')
def cambiar_estado(pedido_id):
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT estado FROM pedidos WHERE id = ?", (pedido_id,))
    pedido = cursor.fetchone()
    if pedido:
        estado_actual = pedido[0]
        nuevo_estado = "Listo para retiro" if estado_actual == "En preparación" else "En preparación"
        cursor.execute("UPDATE pedidos SET estado = ? WHERE id = ?", (nuevo_estado, pedido_id))
        conn.commit()
    conn.close()
    return redirect('/mis-pedidos')

@app.route('/mis-pedidos')
def mis_pedidos():
    conn = sqlite3.connect('pedidos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, producto, total, estado FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return render_template('mis_pedidos.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)
