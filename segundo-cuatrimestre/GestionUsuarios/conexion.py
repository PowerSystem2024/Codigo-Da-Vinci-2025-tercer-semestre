import psycopg2
from psycopg2 import pool
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Conexion:
    _DATABASE = 'postgres'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                logger.info("Pool de conexiones creado")
                return cls._pool
            except Exception as e:
                logger.error(f"Error al crear pool: {e}")
                raise
        return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        logger.debug("Conexión obtenida")
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        logger.debug("Conexión liberada")

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
        logger.info("Todas las conexiones cerradas")