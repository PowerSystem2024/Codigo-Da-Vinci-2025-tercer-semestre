import json
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer

# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="gastos",
    user="admin",
    password="admin123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
)
""")
conn.commit()

class RequestHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(content_length)

        try:
            datos = json.loads(data)
            if self.path == '/register':
                self.registrar_usuario(datos)
            elif self.path == '/login':
                self.iniciar_sesion(datos)
            elif self.path == '/mis-pedidos':
                usuario_id = datos.get('usuario_id')
                if usuario_id:
                    self.ver_pedidos(usuario_id)
                else:
                    self.responder(400, {'message': 'Falta el ID de usuario'})
            else:
                self.responder(404, {'message': 'Ruta no encontrada'})
        except json.JSONDecodeError:
            self.responder(400, {'message': 'JSON inválido'})

    def registrar_usuario(self, datos):
        nombre = datos.get('nombre')
        correo = datos.get('correo')
        contraseña = datos.get('contraseña')

        if not nombre or not correo or not contraseña:
            self.responder(400, {'message': 'Faltan datos'})
            return

        try:
            cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)",
                           (nombre, correo, contraseña))
            conn.commit()
            self.responder(201, {'message': 'Registro exitoso. Ahora podés iniciar sesión.'})
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            self.responder(400, {'message': 'El correo ya está registrado'})
        except Exception as e:
            conn.rollback()
            self.responder(500, {'message': f'Error interno: {str(e)}'})

    def iniciar_sesion(self, datos):
        correo = datos.get('correo')
        contraseña = datos.get('contraseña')

        cursor.execute("SELECT nombre FROM usuarios WHERE correo=%s AND contraseña=%s", (correo, contraseña))
        resultado = cursor.fetchone()

        if resultado:
            self.responder(200, {'message': f'Bienvenido, {resultado[0]}!'})
        else:
            self.responder(401, {'message': 'Correo o contraseña incorrectos'})

    def ver_pedidos(self, usuario_id):
        try:
            cursor.execute("""
                SELECT fecha, punto_retiro, productos, estado
                FROM pedidos
                WHERE usuario_id = %s
                ORDER BY fecha DESC
            """, (usuario_id,))
            resultados = cursor.fetchall()

            pedidos = [
                {
                    'fecha': str(row[0]),
                    'punto_retiro': row[1],
                    'productos': row[2],
                    'estado': row[3]
                }
                for row in resultados
            ]
            self.responder(200, {'pedidos': pedidos})

        except Exception as e:
            self.responder(500, {'message': f'Error al obtener pedidos: {str(e)}'})

    def responder(self, status, data):
        self._set_headers(status)
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    servidor = HTTPServer(('0.0.0.0', 8000), RequestHandler)
    print('Servidor activo en http://localhost:8000')
    servidor.serve_forever()
