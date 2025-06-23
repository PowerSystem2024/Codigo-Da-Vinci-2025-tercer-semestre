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

-- Usuarios de prueba
INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Juan Pérez', 'juan@example.com', '1234'),
('Ana Gómez', 'ana@example.com', '4567');

-- Productos de prueba (asociados a los usuarios de prueba)
INSERT INTO productos (nombre, precio, categoria, descripcion, usuario_id) VALUES
('Notebook', 350000.00, 'Tecnología', 'Laptop Lenovo IdeaPad 3', 1),
('Auriculares', 20000.00, 'Accesorios', 'Auriculares bluetooth Xiaomi', 1),
('Mochila', 15000.00, 'Indumentaria', 'Mochila negra para notebook', 2),
('Mouse inalámbrico', 8000.00, 'Accesorios', 'Mouse Logitech', 2),
('Botella térmica', 9500.00, 'Hogar', 'Botella de acero inoxidable', 1);
