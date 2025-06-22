from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import bcrypt

app = Flask(__name__)
CORS(app)

def init_db():
    with sqlite3.connect("usuarios.db") as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)

# Agregamos un usuario de prueba
def insertar_usuario_prueba():
    with sqlite3.connect("usuarios.db") as con:
        hashed_pw = bcrypt.hashpw("1234".encode('utf-8'), bcrypt.gensalt())
        con.execute("""
            INSERT OR IGNORE INTO usuarios (email, password)
            VALUES (?, ?)
        """, ("test@mail.com", hashed_pw))

insertar_usuario_prueba()
init_db()

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    with sqlite3.connect("usuarios.db") as con:
        cur = con.cursor()
        cur.execute("SELECT password FROM usuarios WHERE email = ?", (email,))
        result = cur.fetchone()

        if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
            return jsonify({"success": True, "message": "Login correcto"})
        else:
            return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"}), 401

if __name__ == "__main__":
    app.run(debug=True)
