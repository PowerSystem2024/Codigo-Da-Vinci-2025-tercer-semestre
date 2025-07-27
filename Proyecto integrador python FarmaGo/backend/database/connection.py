import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="farmago",
        user="irene",
        password="123456"
    )