const API_BASE = "http://localhost:5000"; // Cambiar si estás en producción

/**
 * Enviar una solicitud HTTP al backend.
 * @param {string} endpoint - Ruta del backend, ej: "/login"
 * @param {string} method - Método HTTP, ej: "POST"
 * @param {Object} data - Datos que se envían (opcional)
 * @returns {Promise<Object>} - Respuesta del backend como JSON
 */
export async function apiFetch(endpoint, method = "GET", data = null) {
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
    },
  };

  if (data) {
    options.body = JSON.stringify(data);
  }

  try {
    const response = await fetch(`${API_BASE}${endpoint}`, options);
    const json = await response.json();

    if (!response.ok) {
      throw new Error(json.message || "Error en la solicitud");
    }

    return json;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
}