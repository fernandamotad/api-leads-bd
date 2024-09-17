from db import Database
import psycopg2

class Negocio:
   def __init__ (self, db = Database) :
    self.db = db


    def inserir_Negocio (self, titulo, vencimento_atualizacao, idlead, etapa, idusuario, descricao=None, previsao_venda=None) :
        #adicionar titulo no modelo logico, tirar data de fechamento
        try:
            connection = db.conectar()
            if connection is None:
                print("Falha ao conectar ao banco de dados.")
                return
            
            cursor = connection.cursor()
            inserir_sql = ''' INSERT TO negocio ( titulo, vencimento_atualizacao, data_inclusao, idlead, etapa, 
            idusuario, descricao=None, previsao_venda=None) VALUES (%s, %s, %s, %s, %s, %s, %s)'''

            cursor.execute(inserir_sql, (
                titulo, 
                vencimento_atualizacao, 
                idlead,
                etapa,
                idusuario, 
                descricao if descricao else None, 
                previsao_venda if previsao_venda else None
            ))
            connection.commit()
            print(f'Novo negócio do negocio {idlead.nome} foi cadastrado com sucesso!')
        
        except Exception as e:
           print("Erro ao inserir Negocio:", e)                
        finally:
            if connection:
                cursor.close()
                connection.close()


    def consultar_negocio(self, titulo_ou_id_negocio):
            try:
                connection = self.db.conectar()
                if connection is None:
                    print("Falha ao conectar ao banco de dados.")
                    return
                
                cursor = connection.cursor()
                consultar_sql = '''
                    SELECT * FROM negocio WHERE titulo = %s OR id_negocio = %s;
                '''
                cursor.execute(consultar_sql, (titulo_ou_id_negocio, titulo_ou_id_negocio))
                negocio = cursor.fetchone()
                if negocio:
                    print(f'Negocio encontrado: ID: {negocio[0]}, Nome: {negocio[1]}, Telefone: {negocio[2]}, Telefone Adicional: {negocio[3]}, Email: {negocio[4]}, Anotação: {negocio[5]}')
                else:
                    print(f'negocio {titulo_ou_id_negocio} não encontrado.')
            except (Exception, psycopg2.Error) as error:
                print("Erro ao consultar negocio:", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()

    def listar_todos_negocios(self):
        try:
                connection = self.db.conectar()
                if connection is None:
                    print("Falha ao conectar ao banco de dados.")
                    return
                else:
                    cursor = connection.cursor()
                    consultar_sql = '''SELECT * FROM negocio %s;'''
                    cursor.execute(consultar_sql)
        except (Exception, psycopg2.Error) as e:
                print("Erro ao consultar banco de dados:", e)
        finally:
            if connection:
                    cursor.close()
                    connection.close()



   