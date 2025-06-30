--TABLA DE INIT_DB COMPLETA--

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);

-- Tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    categoria TEXT NOT NULL,
    descripcion TEXT,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    punto_retiro TEXT NOT NULL,
    productos TEXT NOT NULL,
    estado TEXT NOT NULL
);

-- Datos de prueba
INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Juan Pérez', 'juan@example.com', '1234'),
('Ana Gómez', 'ana@example.com', '4567');

<<<<<<< HEAD
INSERT INTO productos (nombre, precio, categoria, descripcion, usuario_id) VALUES
('Notebook', 350000.00, 'Tecnología', 'Laptop Lenovo IdeaPad 3', 1),
('Auriculares', 20000.00, 'Accesorios', 'Auriculares bluetooth Xiaomi', 1),
('Mochila', 15000.00, 'Indumentaria', 'Mochila negra para notebook', 2),
('Mouse inalámbrico', 8000.00, 'Accesorios', 'Mouse Logitech', 2),
('Botella térmica', 9500.00, 'Hogar', 'Botella de acero inoxidable', 1);

INSERT INTO pedidos (usuario_id, punto_retiro, productos, estado) VALUES
(1, 'Sucursal Centro', 'Notebook, Auriculares', 'Entregado'),
(1, 'Sucursal Norte', 'Mouse inalámbrico', 'Pendiente'),
(2, 'Sucursal Sur', 'Botella térmica', 'En camino');
=======
-- Productos de farmacia
INSERT INTO productos (nombre, precio, categoria, descripcion, usuario_id) VALUES
('Ibuprofeno 400mg', 1500.00, 'Medicamento', 'Caja con 10 comprimidos', 1),
('Paracetamol 500mg', 1300.00, 'Medicamento', 'Analgésico y antipirético', 1),
('Alcohol en gel 250ml', 2200.00, 'Higiene', 'Antibacterial para manos', 2),
('Termómetro digital', 4800.00, 'Instrumental', 'Para temperatura corporal', 2),
('Té digestivo', 950.00, 'Fitoterapia', 'Caja con 20 saquitos', 1);

-- Pedidos de farmacia
INSERT INTO pedidos (usuario_id, punto_retiro, productos, estado) VALUES
(1, 'Farmacia Central', 'Ibuprofeno 400mg, Té digestivo', 'Entregado'),
(1, 'Sucursal Este', 'Paracetamol 500mg, Alcohol en gel', 'Pendiente'),
(2, 'Sucursal Norte', 'Termómetro digital', 'En camino');

>>>>>>> 96d8896 (Corrijo errores de productos y pedidos en archivos sql)
