document.addEventListener('DOMContentLoaded', async () => {
  const contenedor = document.getElementById("lista-pedidos");
  const usuarioId = localStorage.getItem("usuarioId") || 1;

  const res = await fetch(`/mis-pedidos?usuario_id=${usuarioId}`);
  const data = await res.json();

  if (!data.success) {
    contenedor.textContent = "No se pudieron cargar los pedidos.";
    return;
  }

  if (data.pedidos.length === 0) {
    contenedor.textContent = "Todavía no realizaste pedidos.";
    return;
  }

  data.pedidos.forEach(p => {
    const div = document.createElement("div");
    div.classList.add("pedido");

    const fecha = new Date(p.fecha).toLocaleString();

    div.innerHTML = `
      <p><strong>Fecha:</strong> ${fecha}</p>
      <p><strong>Productos:</strong> ${p.productos}</p>
      <p><strong>Método de pago:</strong> ${p.metodo_pago}</p>
      <p><strong>Total:</strong> $${p.total}</p>
      <hr>
    `;
    div.innerHTML = `
  <p><strong>Fecha:</strong> ${fecha}</p>
  <p><strong>Productos:</strong> ${p.productos}</p>
  <p><strong>Método de pago:</strong> ${p.metodo_pago}</p>
  <p><strong>Total:</strong> $${p.total}</p>
  <p><strong>Estado:</strong> ${p.estado}</p>
  <hr>
`;

    contenedor.appendChild(div);
  });
});