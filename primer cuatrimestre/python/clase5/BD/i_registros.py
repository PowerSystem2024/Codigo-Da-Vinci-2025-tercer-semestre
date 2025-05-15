import psycopg2 # Esto es para poder conectarnos a postgre

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@gmail.com') #es una tupla
            cursor.execute(sentencia, valores) # De esta manera recuperamos la sentencia
            # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertaods son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()