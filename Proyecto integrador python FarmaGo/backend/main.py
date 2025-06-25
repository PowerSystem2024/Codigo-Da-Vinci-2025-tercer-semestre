from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
app = FastAPI()

productos = [
    {"id": 1, "nombre": "Paracetamol", "precio": 5.99, "stock": 100},
    {"id": 2, "nombre": "Ibuprofeno", "precio": 7.50, "stock": 50}
]

@app.get("/productos")
def listar_productos():
    return productos

@app.get("/producto/{id}")
def ver_producto(id: int):
    return next((p for p in productos if p["id"] == id), None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)