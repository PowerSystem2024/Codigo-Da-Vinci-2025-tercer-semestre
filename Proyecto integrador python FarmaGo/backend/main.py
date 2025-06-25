from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic importBaseModel
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock de base de datos
carrito = {}

class ItemCarrito(BaseModel):
    producto_id: int
    cantidad: int

@app.post("/carrito/agregar")
async def agregar_al_carrito(item: ItemCarrito):
    """
    Agrega un producto al carrito
    """
    try:
        if item.producto_id in carrito:
            carrito[item.producto_id] += item.cantidad
        else:
            carrito[item.producto_id] = item.cantidad

        return {"mensaje": "Producto agregado al carrito", "carrito": carrito}
    except Exception as e:
        raise HTTPException(Status_code=400, detail=str(e))

@app.get("/carrito")
async def obtener_carrito():
    """
    Obtiene el contenido del carrito
    """
    return carrito

@app.delete("/carrito/{producto_id}")
async def eliminar_del_carrito(producto_id: int):
    """
    Elimina un producto del carrito
    """
    if producto_id in carrito:
        del carrito[producto_id]
        return {"mensaje": "Producto eliminado del carrito"}
    raise HTTPException(status_code=404, detail="Producto no encontrado en el carrito")

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