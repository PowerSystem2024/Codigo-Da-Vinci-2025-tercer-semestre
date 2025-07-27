
-- =============================
-- Crear tabla de usuarios
-- =============================
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);

-- =============================
-- Crear tabla de productos
-- =============================
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    categoria TEXT NOT NULL,
    stock INTEGER NOT NULL,
    imagen_url TEXT
);

-- =============================
-- Crear tabla de puntos de retiro
-- =============================
CREATE TABLE IF NOT EXISTS puntos_retiro (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    ciudad TEXT,
    provincia TEXT,
    activo BOOLEAN DEFAULT TRUE
);

-- =============================
-- Crear tabla de pedidos
-- =============================
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    punto_retiro_id INTEGER,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    metodo_pago TEXT,
    estado TEXT DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (punto_retiro_id) REFERENCES puntos_retiro(id)
);

-- =============================
-- Crear tabla de detalle_pedidos
-- =============================
CREATE TABLE IF NOT EXISTS detalle_pedidos (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- =============================
-- INSERT de usuarios
-- =============================
INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Irene Machuca', 'irene@mail.com', 'hashedpassword1'),
('Juan Pérez', 'juan@mail.com', 'hashedpassword2'),
('Ana Gómez', 'ana@mail.com', 'hashedpassword3');

-- =============================
-- INSERT de productos
-- =============================
INSERT INTO productos (nombre, descripcion, precio, categoria, stock, imagen_url) VALUES
('Paracetamol', 'Analgésico y antipirético 500mg', 850.00, 'Analgésicos', 100, 'https://via.placeholder.com/100'),
('Ibuprofeno', 'Antiinflamatorio 400mg', 920.00, 'Analgésicos', 80, 'https://via.placeholder.com/100'),
('Amoxicilina', 'Antibiótico 500mg', 1200.00, 'Antibióticos', 50, 'https://via.placeholder.com/100'),
('Vitamina C', 'Refuerza el sistema inmune', 700.00, 'Vitaminas', 150, 'https://via.placeholder.com/100'),
('Aspirina', 'Alivia dolores leves', 780.00, 'Analgésicos', 90, 'https://via.placeholder.com/100');

-- =============================
-- INSERT de puntos de retiro
-- =============================
INSERT INTO puntos_retiro (nombre, direccion, ciudad, provincia) VALUES
('Farmacia Central', 'Av. Siempre Viva 123', 'Buenos Aires', 'Buenos Aires'),
('Farmacia Norte', 'Calle Falsa 456', 'Córdoba', 'Córdoba'),
('Farmacia Sur', 'Av. del Sol 789', 'Mendoza', 'Mendoza');

-- =============================
-- INSERT de pedidos (opcional de ejemplo)
-- =============================
INSERT INTO pedidos (usuario_id, punto_retiro_id, total, metodo_pago) VALUES
(1, 1, 1570.00, 'Efectivo'),
(2, 2, 920.00, 'Tarjeta');

-- =============================
-- INSERT de detalle_pedidos (opcional de ejemplo)
-- =============================
INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 1, 850.00),
(1, 4, 1, 700.00),
(2, 2, 1, 920.00);