from conexion import Conexion
import logging

logger = logging.getLogger(__name__)


class CursorDelPool:
    def __enter__(self):
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        logger.debug("Cursor creado")
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conexion.rollback()
            logger.error(f"Error: {exc_val}")
        else:
            self._conexion.commit()
            logger.debug("Transacción exitosa")

        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)
        logger.debug("Recursos liberados")