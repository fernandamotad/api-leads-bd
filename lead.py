import psycopg2
from db import Database

class Lead:
    def __init__(self, db: Database):
        self.db = db

    def inserir_lead(self, nome, telefone, telefone_adicional=None, email=None, anotacao=None):
        try:
            connection = self.db.conectar()
            if connection is None:
                print("Falha ao conectar ao banco de dados.")
                return
            
            cursor = connection.cursor()
            inserir_sql = '''
                INSERT INTO lead (nome, telefone, telefone_adicional, email, anotacao)
                VALUES (%s, %s, %s, %s, %s);
            '''
            
            # Insere None se os valores opcionais forem vazios
            cursor.execute(inserir_sql, (
                nome, 
                telefone, 
                telefone_adicional if telefone_adicional else None, 
                email if email else None, 
                anotacao if anotacao else None
            ))
            connection.commit()
            print(f'O lead {nome} foi cadastrado com sucesso!')
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir lead:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def consultar_lead(self, nome_ou_telefone):
        try:
            connection = self.db.conectar()
            if connection is None:
                print("Falha ao conectar ao banco de dados.")
                return
            
            cursor = connection.cursor()
            consultar_sql = '''
                SELECT * FROM lead WHERE nome = %s OR telefone = %s;
            '''
            cursor.execute(consultar_sql, (nome_ou_telefone, nome_ou_telefone))
            lead = cursor.fetchone()
            if lead:
                print(f'Lead encontrado: ID: {lead[0]}, Nome: {lead[1]}, Telefone: {lead[2]}, Telefone Adicional: {lead[3]}, Email: {lead[4]}, Anotação: {lead[5]}')
            else:
                print(f'Lead {nome_ou_telefone} não encontrado.')
        except (Exception, psycopg2.Error) as error:
            print("Erro ao consultar lead:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def listar_todos_leads(self):
        try:
            connection = self.db.conectar()
            if connection is None:
                print("Falha ao conectar ao banco de dados.")
                return

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM lead;")
            leads = cursor.fetchall()
            if leads:
                for lead in leads:
                    print(f'ID: {lead[0]}, Nome: {lead[1]}, Telefone: {lead[2]}, Telefone Adicional: {lead[3]}, Email: {lead[4]}, Anotação: {lead[5]}')
            else:
                print("Nenhum lead encontrado.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao listar leads:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
