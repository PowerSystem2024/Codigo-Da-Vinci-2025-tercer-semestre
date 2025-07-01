def agregar_producto(carrito, producto_id, cantidad=1):
    if str(producto_id) in carrito:
        carrito[str(producto_id)] += cantidad
    else:
        carrito[str(producto_id)] = cantidad
    return carrito

def obtener_detalle_carrito(carrito, productos_db):
    detalle = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = productos_db.get(int(producto_id))
        if producto:
            subtotal = cantidad * producto['precio']
            detalle.append({
                'id': producto_id,
                'nombre': producto['nombre'],
                'precio': producto['precio'],
                'cantidad': cantidad,
                'subtotal': subtotal
            })
            total += subtotal

    return detalle, total