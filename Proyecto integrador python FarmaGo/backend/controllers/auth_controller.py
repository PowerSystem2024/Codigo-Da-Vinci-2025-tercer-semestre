import bcrypt
from database.connection import get_connection

def registrar_usuario(data):
    nombre = data.get("nombre")
    correo = data.get("correo")
    contraseña = data.get("contraseña")
    
    if not all([nombre, correo, contraseña]):
        return {"success": False, "message": "Faltan datos"}

    hashed_pw = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña)
            VALUES (%s, %s, %s)
        """, (nombre, correo, hashed_pw))
        conn.commit()
        cur.close()
        conn.close()
        return {"success": True, "message": "Registro exitoso"}
    except psycopg2.errors.UniqueViolation:
        return {"success": False, "message": "Correo ya registrado"}
    except Exception as e:
        return {"success": False, "message": str(e)}
    



def iniciar_sesion(data):
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    if not correo or not contraseña:
        return {'success': False, 'message': 'Faltan datos'}

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT contraseña FROM usuarios WHERE correo = %s", (correo,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row and bcrypt.checkpw(contraseña.encode('utf-8'), row[0].encode('utf-8')):
            return {'success': True, 'message': 'Login exitoso'}
        else:
            return {'success': False, 'message': 'Correo o contraseña incorrectos'}

    except Exception as e:
        return {'success': False, 'message': f'Error interno: {str(e)}'}

def recuperar_contraseña(data):
    correo = data.get('correo')

    if not correo:
        return {'success': False, 'message': 'Debe ingresar un correo'}

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM usuarios WHERE correo = %s", (correo,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return {'success': True, 'message': f'Se envió un email de recuperación a {correo} (simulado).'}
        else:
            return {'success': False, 'message': 'Correo no registrado'}

    except Exception as e:
        return {'success': False, 'message': f'Error interno: {str(e)}'}