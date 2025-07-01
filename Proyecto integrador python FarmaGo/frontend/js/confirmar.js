document.addEventListener('DOMContentLoaded', () => {
  const pedido = JSON.parse(localStorage.getItem('carrito')) || [];
  const usuarioId = localStorage.getItem('usuarioId') || 1; // Suponiendo sesión ficticia
  const resumenDiv = document.getElementById('resumen-pedido');

  let total = 0;
  pedido.forEach(p => {
    total += p.precio * p.cantidad;
    const item = document.createElement('p');
    item.textContent = `${p.nombre} x ${p.cantidad} = $${p.precio * p.cantidad}`;
    resumenDiv.appendChild(item);
  });

  const totalP = document.createElement('p');
  totalP.innerHTML = `<strong>Total: $${total}</strong>`;
  resumenDiv.appendChild(totalP);

  window.confirmarPedido = async () => {
    const metodo = document.getElementById('metodo-pago').value;
    const msg = document.getElementById('msg');

    if (!metodo) {
      msg.textContent = 'Seleccioná un método de pago.';
      return;
    }

    const res = await fetch('/confirmar-pedido', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        usuario_id: usuarioId,
        productos: pedido,
        total,
        metodo_pago: metodo
      })
    });

    const data = await res.json();
    msg.textContent = data.message;

    if (data.success) {
      localStorage.removeItem('carrito');
    }
  };
});