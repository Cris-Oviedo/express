import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host= 'localhost',
            user= 'postgres',
            password= 'qwerty',
            database= 'db'
        )
        print("Conexión exitosa ")
    except Exception as ex:
        print(f"Error al conectar {ex}")