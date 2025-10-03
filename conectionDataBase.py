import psycopg

try:
    conection = psycopg.connect(
        dbname="postgres",
        user="postgres",
        host='localhost',
        password="123",
        port=5432
    )
    print("Conexão bem-sucedida!")

except psycopg.ProgrammingError as e:
    print(f"Erro de programação: {e}")
except psycopg.OperationalError as e:
    print(f"Erro de operação: {e}")