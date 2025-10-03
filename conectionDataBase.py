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

def verifyTable():
    cursor = conection.cursor()
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = "DataModel"
        );
    """, )
    exists = cursor.fetchone()[0]
    cursor.close()
    return exists

def createTable():
    cursor = conection.cursor()
    cursor.execute("""
        CREATE TABLE DATAMODEL (
            id SERIAL PRIMARY KEY,
            date timestamp,
            energy_generation numeric,
            temperature numeric,
            performance numeric
            )
    """,)
    cursor.close()
    return print("Tabela criada com sucesso!")


if verifyTable():
    print("Tabela existe!")
else:
    createTable()