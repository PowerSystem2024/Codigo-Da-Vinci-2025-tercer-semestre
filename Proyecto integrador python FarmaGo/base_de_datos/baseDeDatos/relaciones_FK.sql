-- relaciones_FK.sql

ALTER TABLE pedidos
ADD CONSTRAINT fk_usuario
FOREIGN KEY (usuario_id) REFERENCES usuarios(id);

ALTER TABLE detalle_pedidos
ADD CONSTRAINT fk_pedido
FOREIGN KEY (pedido_id) REFERENCES pedidos(id);

ALTER TABLE detalle_pedidos
ADD CONSTRAINT fk_producto
FOREIGN KEY (producto_id) REFERENCES productos(id);