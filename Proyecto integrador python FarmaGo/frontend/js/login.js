import { apiFetch } from "./api.js";

async function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const resultado = await apiFetch("/login", "POST", {
      correo: email,
      contraseña: password,
    });

    alert(resultado.message);
    // Redirigir si es necesario
  } catch (error) {
    alert("Error al iniciar sesión: " + error.message);
  }
}