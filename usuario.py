from db import Database
import psycopg2 

class Usuario:
    def __init__(self, db: Database):
        self.db = db

    def inserir_usuario(self, nivel, nome, login, senha):
        try:
            connection = self.db.conectar()
            cursor = connection.cursor()
            inserir_sql = 'INSERT INTO usuario (nivel_de_acesso, nome, login, senha) VALUES (%s, %s, %s, %s);'
            cursor.execute(inserir_sql, (nivel, nome, login, senha))
            connection.commit()
            print(f'O usuário {nome} foi cadastrado com sucesso!')
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def consultar_usuario(self, login_nome):
        try:
            connection = self.db.conectar()
            cursor = connection.cursor()
            consultar_sql = 'SELECT * FROM usuario WHERE login = %s OR nome = %s;'
            cursor.execute(consultar_sql, (login_nome, login_nome))
            usuario = cursor.fetchone()
            if usuario:
                print(f'Usuário {usuario[2]} cadastrado')
            else:
                print(f'Usuário {login_nome} não cadastrado')
        except (Exception, psycopg2.Error) as error:
            print("Erro ao consultar dados:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def listar_todos_usuarios(self):
        try:
            connection = self.db.conectar()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario;")
            usuarios = cursor.fetchall()
            if usuarios:
                for usuario in usuarios:
                    print(f'ID: {usuario[0]}, Nome: {usuario[2]}, Login: {usuario[3]}, Nível de Acesso: {usuario[1]}')
            else:
                print("Nenhum usuário encontrado.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao consultar usuários:", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
