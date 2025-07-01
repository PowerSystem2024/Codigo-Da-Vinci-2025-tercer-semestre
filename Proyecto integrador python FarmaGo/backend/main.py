from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import sqlite3
from geopy.distance import geodesic

app = FastAPI(title="Farmago API", version="1.0.0")

# Configuración CORS (simplificada y sin duplicados)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Modelos Pydantic ---
class ItemCarrito(BaseModel):
    producto_id: int
    cantidad: int
    punto_retiro_id: Optional[int] = None  # Nuevo campo para punto de retiro


class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None


class PuntoRetiro(BaseModel):
    id: int
    nombre: str
    direccion: str
    ciudad: str
    provincia: str
    horario: str
    latitud: Optional[float] = None
    longitud: Optional[float] = None


class PuntoRetiroConStock(PuntoRetiro):
    stock: int
    distancia: Optional[str] = None


# --- Base de datos simple ---
def get_db():
    conn = sqlite3.connect('farmago.db')
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with sqlite3.connect('farmago.db') as conn:
        cursor = conn.cursor()
        # Tabla de productos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            descripcion TEXT,
            imagen_url TEXT
        )''')

        # Tabla de puntos de retiro
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS puntos_retiro (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            ciudad TEXT NOT NULL,
            provincia TEXT NOT NULL,
            horario TEXT DEFAULT 'Lunes a Viernes 9:00-18:00',
            latitud REAL,
            longitud REAL,
            activo BOOLEAN DEFAULT 1
        )''')

        # Tabla de stock por punto de retiro
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_puntos_retiro (
            id INTEGER PRIMARY KEY,
            punto_retiro_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            stock INTEGER DEFAULT 0,
            FOREIGN KEY(punto_retiro_id) REFERENCES puntos_retiro(id),
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )''')

        # Datos iniciales
        cursor.execute("SELECT COUNT(*) FROM productos")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO productos (id, nombre, precio, stock) VALUES (?, ?, ?, ?)",
                [(1, "Paracetamol", 5.99, 100), (2, "Ibuprofeno", 7.50, 50)]
            )

            cursor.executemany(
                "INSERT INTO puntos_retiro (id, nombre, direccion, ciudad, provincia) VALUES (?, ?, ?, ?, ?)",
                [
                    (1, "Farmago Centro", "Av. Principal 123", "Ciudad", "Provincia"),
                    (2, "Farmago Norte", "Calle Secundaria 456", "Ciudad", "Provincia")
                ]
            )

            cursor.executemany(
                "INSERT INTO stock_puntos_retiro (punto_retiro_id, producto_id, stock) VALUES (?, ?, ?)",
                [
                    (1, 1, 20), (1, 2, 15),
                    (2, 1, 10), (2, 2, 5)
                ]
            )

        conn.commit()


# Inicializar la base de datos al iniciar
init_db()


# --- Endpoints existentes mejorados ---
@app.post("/carrito/agregar")
async def agregar_al_carrito(item: ItemCarrito, db: Depends(get_db)):
    """Agrega un producto al carrito con opción de punto de retiro"""
    try:
        cursor = db.cursor()

        # Verificar stock si se seleccionó punto de retiro
        if item.punto_retiro_id:
            cursor.execute('''
                SELECT stock FROM stock_puntos_retiro 
                WHERE producto_id = ? AND punto_retiro_id = ?
            ''', (item.producto_id, item.punto_retiro_id))
            stock = cursor.fetchone()

            if not stock or stock[0] < item.cantidad:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Stock insuficiente en el punto de retiro seleccionado"
                )

        # Lógica del carrito (simplificada para el ejemplo)
        cursor.execute('''
            INSERT OR REPLACE INTO carrito (producto_id, cantidad, punto_retiro_id)
            VALUES (?, COALESCE((SELECT cantidad FROM carrito WHERE producto_id = ?), 0) + ?, ?)
        ''', (item.producto_id, item.producto_id, item.cantidad, item.punto_retiro_id))

        db.commit()
        return {"mensaje": "Producto agregado al carrito"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@app.get("/carrito")
async def obtener_carrito(db: Depends(get_db)):
    """Obtiene el contenido del carrito"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM carrito")
    return {
        "items": [
            {"producto_id": row[0], "cantidad": row[1], "punto_retiro_id": row[2]}
            for row in cursor.fetchall()
        ]
    }


# --- Nuevos endpoints para puntos de retiro ---
@app.get("/puntos-retiro", response_model=List[PuntoRetiro])
async def listar_puntos_retiro(db: Depends(get_db)):
    """Lista todos los puntos de retiro activos"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM puntos_retiro WHERE activo = 1")
    return [
        PuntoRetiro(
            id=row[0], nombre=row[1], direccion=row[2],
            ciudad=row[3], provincia=row[4], horario=row[5],
            latitud=row[6], longitud=row[7]
        )
        for row in cursor.fetchall()
    ]


@app.get("/puntos-retiro/con-stock/{producto_id}", response_model=List[PuntoRetiroConStock])
async def puntos_retiro_con_stock(
        producto_id: int,
        lat: Optional[float] = None,
        lng: Optional[float] = None,
        db: Depends(get_db)
):
    """Lista puntos de retiro con stock para un producto, ordenados por distancia"""
    cursor = db.cursor()
    cursor.execute('''
        SELECT pr.*, spr.stock 
        FROM puntos_retiro pr
        JOIN stock_puntos_retiro spr ON pr.id = spr.punto_retiro_id
        WHERE spr.producto_id = ? AND spr.stock > 0 AND pr.activo = 1
    ''', (producto_id,))

    puntos = []
    for row in cursor.fetchall():
        punto = PuntoRetiroConStock(
            id=row[0], nombre=row[1], direccion=row[2],
            ciudad=row[3], provincia=row[4], horario=row[5],
            latitud=row[6], longitud=row[7], stock=row[8]
        )

        # Calcular distancia si se proporcionan coordenadas
        if lat and lng and row[6] and row[7]:
            distancia_km = geodesic((lat, lng), (row[6], row[7])).kilometers
            punto.distancia = f"{distancia_km:.1f} km"

        puntos.append(punto)

    # Ordenar por distancia si hay coordenadas
    if lat and lng:
        puntos.sort(key=lambda x: float(x.distancia.split()[0]) if x.distancia else float('inf'))

    return puntos


# --- Endpoints existentes para productos ---
@app.get("/productos", response_model=List[Producto])
def listar_productos(db: Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos")
    return [
        Producto(
            id=row[0], nombre=row[1], precio=row[2],
            stock=row[3], descripcion=row[4], imagen_url=row[5]
        )
        for row in cursor.fetchall()
    ]


@app.get("/producto/{id}", response_model=Producto)
def ver_producto(id: int, db: Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return Producto(
        id=row[0], nombre=row[1], precio=row[2],
        stock=row[3], descripcion=row[4], imagen_url=row[5]
    )

