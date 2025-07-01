document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const correo = document.getElementById('correo').value.trim();
    const contraseña = document.getElementById('contraseña').value.trim();
    const mensajeDiv = document.getElementById('mensaje');

    if (!correo || !contraseña) {
        mensajeDiv.textContent = 'Por favor, complete todos los campos.';
        return;
    }

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ correo, contraseña })
        });

        const data = await response.json();

        if (response.ok) {
            mensajeDiv.textContent = 'Login exitoso. Redirigiendo...';
            // Redirigir a home u otra página
            setTimeout(() => window.location.href = 'index.html', 1500);
        } else {
            mensajeDiv.textContent = data.message || 'Error en login.';
        }

    } catch (error) {
        mensajeDiv.textContent = 'Error en la comunicación con el servidor.';
    }
});