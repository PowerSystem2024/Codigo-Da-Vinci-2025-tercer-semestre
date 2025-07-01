CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio NUMERIC NOT NULL,
    categoria TEXT NOT NULL,
    imagen_url TEXT
);

---Insercion:

INSERT INTO productos (nombre, descripcion, precio, categoria, imagen_url) VALUES
('Ibuprofeno', 'Analgésico y antiinflamatorio', 850.0, 'analgésicos', 'https://via.placeholder.com/100'),
('Vitamina C', 'Refuerza el sistema inmune', 700.0, 'vitaminas', 'https://via.placeholder.com/100');

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    metodo_pago VARCHAR(50),
    estado VARCHAR(50) DEFAULT 'pendiente'
);

CREATE TABLE IF NOT EXISTS detalle_pedidos (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL
);