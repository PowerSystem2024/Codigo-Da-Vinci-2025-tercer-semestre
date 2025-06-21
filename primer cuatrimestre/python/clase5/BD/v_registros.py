import psycopg2 # Esto es para poder conectarnos a postgre

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #Placeholder
            entrada = input('Digite los id persona a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves_primarias) # De esta manera recuperamos la sentencia
            registros = cursor.fetchall() # Recuperamos todos los registros que seran una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()