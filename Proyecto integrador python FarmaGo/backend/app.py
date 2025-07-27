from flask import Flask
from flask_cors import CORS

# Blueprints (rutas)
from routes.register import register_bp
from routes.login import login_bp
from routes.recuperar import recuperar_bp
from routes.productos import productos_bp
from routes.detalle_producto import detalle_producto_bp
from routes.pedidos import pedidos_bp
from routes.carrito import carrito_bp
from routes.puntos_retiro import puntos_retiro_bp


app = Flask(__name__)
CORS(app)

# Registro de Blueprints
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(recuperar_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(detalle_producto_bp)
app.register_blueprint(pedidos_bp)
app.register_blueprint(carrito_bp)
app.register_blueprint(puntos_retiro_bp)

if __name__ == "__main__":
    app.run(debug=True)

