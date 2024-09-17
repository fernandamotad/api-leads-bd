import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, host, database, user, password, port="5432"):
        self.host = os.getenv('host')
        self.database = "Multiple-lead"
        self.user = os.getenv('user')
        self.password = os.getenv('password')
        self.port = '5432'
    
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
