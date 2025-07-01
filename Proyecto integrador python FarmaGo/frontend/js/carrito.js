async function obtenerCarrito() {
    const response = await fetch('/carrito');
    const data = await response.json();
    mostrarCarrito(data.carrito);
}

function mostrarCarrito(carrito) {
    const contenedor = document.getElementById('carrito-container');
    contenedor.innerHTML = '';

    if (!carrito || Object.keys(carrito).length === 0) {
        contenedor.innerHTML = '<p>El carrito está vacío</p>';
        return;
    }

    const ul = document.createElement('ul');
    for (const [productoId, cantidad] of Object.entries(carrito)) {
        const li = document.createElement('li');
        li.textContent = `Producto ID: ${productoId} - Cantidad: ${cantidad}`;
        ul.appendChild(li);
    }
    contenedor.appendChild(ul);
}

async function vaciarCarrito() {
    // Si querés, agregamos backend para vaciar carrito. Por ahora limpia session frontend
    alert('Vaciar carrito: Implementar backend o localStorage');
}

document.addEventListener('DOMContentLoaded', obtenerCarrito);

document.addEventListener('DOMContentLoaded', async () => {
  const res = await fetch('/carrito');
  const data = await res.json();
  mostrarCarrito(data.items, data.total);
});

function mostrarCarrito(items, total) {
  const contenedor = document.getElementById('carrito-container');
  const totalP = document.getElementById('total');
  
  if (!items || items.length === 0) {
    contenedor.innerHTML = '<p>El carrito está vacío.</p>';
    totalP.textContent = '';
    return;
  }

  const table = document.createElement('table');
  table.innerHTML = `
    <tr>
      <th>Producto</th>
      <th>Precio</th>
      <th>Cantidad</th>
      <th>Subtotal</th>
    </tr>
  `;

  items.forEach(item => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${item.nombre}</td>
      <td>$${item.precio.toFixed(2)}</td>
      <td>${item.cantidad}</td>
      <td>$${item.subtotal.toFixed(2)}</td>
    `;
    table.appendChild(row);
  });
contenedor.appendChild(table);
  totalP.textContent = `Total: $${total.toFixed(2)}`;
}

document.addEventListener('DOMContentLoaded', () => {
  cargarPuntosRetiro();
  cargarCarrito();
});

async function cargarPuntosRetiro() {
  const res = await fetch('/puntos-retiro');
  const puntos = await res.json();

  const select = document.getElementById('punto-retiro');
  puntos.forEach(p => {
    const opt = document.createElement('option');
    opt.value = p.id;
    opt.textContent = `${p.nombre} - ${p.direccion}`;
    select.appendChild(opt);
  });

  // Cargar punto de retiro guardado
  const puntoGuardado = localStorage.getItem('puntoRetiro');
  if (puntoGuardado) {
    select.value = puntoGuardado;
  }

  select.addEventListener('change', () => {
    localStorage.setItem('puntoRetiro', select.value);
  });
}

async function cargarCarrito() {
  const res = await fetch('/carrito');
  const data = await res.json();
  mostrarCarrito(data.items, data.total);
}

function mostrarCarrito(items, total) {
  const contenedor = document.getElementById('carrito-container');
  const totalP = document.getElementById('total');
  contenedor.innerHTML = '';

  if (!items || items.length === 0) {
    contenedor.innerHTML = '<p>El carrito está vacío.</p>';
    totalP.textContent = '';
    return;
  }

  const table = document.createElement('table');
  table.innerHTML = `
    <tr>
      <th>Producto</th>
      <th>Precio</th>
      <th>Cantidad</th>
      <th>Subtotal</th>
    </tr>
  `;

  items.forEach(item => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${item.nombre}</td>
      <td>$${item.precio.toFixed(2)}</td>
      <td>${item.cantidad}</td>
      <td>$${item.subtotal.toFixed(2)}</td>
    `;
    table.appendChild(row);
  });

  contenedor.appendChild(table);
  totalP.textContent = `Total: $${total.toFixed(2)}`;
}
