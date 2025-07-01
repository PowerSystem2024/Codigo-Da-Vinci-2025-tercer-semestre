document.addEventListener("DOMContentLoaded", () => {
  const selectCategoria = document.getElementById("categoriaFiltro");
  const contenedor = document.getElementById("productos");

  function cargarProductos(categoria = "") {
    let url = "http://localhost:5000/productos";
    if (categoria) url += `?categoria=${encodeURIComponent(categoria)}`;

    fetch(url)
      .then(res => res.json())
      .then(data => {
        contenedor.innerHTML = "";
        if (data.length === 0) {
          contenedor.innerHTML = "<p>No hay productos en esta categoría.</p>";
          return;
        }
        data.forEach(prod => {
          contenedor.innerHTML += `
            <div class="producto">
              <img src="${prod.imagen_url}" alt="${prod.nombre}" />
              <h3>${prod.nombre}</h3>
              <p>${prod.descripcion}</p>
              <p>$${prod.precio}</p>
            </div>
          `;
        });
      });
  }

  selectCategoria.addEventListener("change", () => {
    cargarProductos(selectCategoria.value);
  });

  cargarProductos();
});