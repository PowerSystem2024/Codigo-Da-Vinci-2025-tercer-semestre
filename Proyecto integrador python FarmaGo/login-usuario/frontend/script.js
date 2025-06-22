function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        alert("Login exitoso 🚀");
        // Podés redirigir al home acá
      } else {
        alert("Error: " + data.message);
      }
    })
    .catch(err => {
      alert("Error de conexión");
      console.error(err);
    });
}
