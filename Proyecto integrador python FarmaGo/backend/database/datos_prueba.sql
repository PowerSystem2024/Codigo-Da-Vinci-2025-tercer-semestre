-- datos_prueba.sql

-- Usuarios de prueba
INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Irene Machuca', 'irene@mail.com', 'hashedpassword1'),
('Juan Pérez', 'juan@mail.com', 'hashedpassword2'),
('Ana Gómez', 'ana@mail.com', 'hashedpassword3');

-- Productos de prueba
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Paracetamol', 'Analgésico y antipirético', 5.99, 100),
('Ibuprofeno', 'Antiinflamatorio', 7.50, 50),
('Amoxicilina', 'Antibiótico', 12.30, 30),
('Vitamina C', 'Suplemento vitamínico', 8.00, 75),
('Aspirina', 'Analgésico y antiinflamatorio', 6.20, 80);