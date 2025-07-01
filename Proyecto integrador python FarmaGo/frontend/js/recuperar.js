document.getElementById('recuperarForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const correo = document.getElementById('correo').value.trim();
    const mensajeDiv = document.getElementById('mensaje');

    if (!correo) {
        mensajeDiv.textContent = 'Por favor ingrese su correo.';
        return;
    }

    try {
        const response = await fetch('/recuperar', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ correo })
        });

        const data = await response.json();

        if (response.ok) {
            mensajeDiv.textContent = data.message;
        } else {
            mensajeDiv.textContent = data.message || 'Error al recuperar la contraseña.';
        }
    } catch (error) {
        mensajeDiv.textContent = 'Error de comunicación con el servidor.';
    }
});