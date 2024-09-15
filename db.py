import psycopg2

class Database:
    def __init__(self, host, database, user, password, port="5432"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
    
    def conectar(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            return connection
        except (Exception, psycopg2.Error) as error:
            print(f"Erro ao conectar ao banco de dados: {error}")
            return None
