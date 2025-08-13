import logging

# Configuración básica del logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app_usuarios.log',
    filemode='a'
)

log = logging.getLogger(__name__)