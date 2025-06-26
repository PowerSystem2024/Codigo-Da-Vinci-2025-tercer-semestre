CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    punto_retiro TEXT NOT NULL,
    productos TEXT NOT NULL, -- Lista tipo string por simplicidad
    estado TEXT NOT NULL     -- Ej: "Pendiente", "En camino", "Entregado"
);