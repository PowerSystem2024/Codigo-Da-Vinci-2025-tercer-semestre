import psycopg2 as bd # Esto es para poder conectarnos a postgre
from psycopg2 import connect

conexion = bd.connect(user='postgres',password='tatito11',host='127.0.0.1',port='5432',database='test_bd')
try:
    #conexion.autocommit = False # esto directamente no deberia estar
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('María', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  #Hacemos el commit manualmente
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()