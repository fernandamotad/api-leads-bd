from db import Database
import psycopg2

class Negocio:
    def __init__ (self, db = Database) :
        self.db = db


    def inserir_negocio(self, titulo, vencimento_atualizacao, idlead, etapa, idusuario, descricao=None, previsao_venda=None) :
        
        from datetime import datetime

        #adicionar titulo no modelo logico, tirar data de fechamento
        try:
            connection = self.db.conectar()
            if connection is None:
                print("Falha ao conectar ao banco de dados.")
                return
            
            cursor = connection.cursor()

            vencimento_atualizacao_formatada = datetime.strptime(vencimento_atualizacao, '%d/%m/%Y').date()

            inserir_sql = ''' INSERT INTO negocio ( titulo, vencimento_atualizacao, data_inclusao, idlead, etapa, 
            idusuario, descricao, previsao_venda) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

            cursor.execute(inserir_sql, (
                titulo, 
                vencimento_atualizacao_formatada,
                datetime.now(), 
                idlead,
                etapa,
                idusuario, 
                descricao if descricao else None, 
                previsao_venda if previsao_venda else None
            ))
            connection.commit()
            print(f'O negócio {titulo} foi cadastrado com sucesso!')
        
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

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM negocio;")
            negocios = cursor.fetchall()

            if negocios:
                for negocio in negocios:
                    # Ajuste a ordem e os campos conforme a estrutura da tabela 'negocio'
                    print(f'ID: {negocio[0]}, Título: {negocio[1]}, Vencimento Atualização: {negocio[2]}, Data Inclusão: {negocio[3]}, '
                        f'ID Lead: {negocio[4]}, Etapa: {negocio[5]}, ID Usuário: {negocio[6]}, Descrição: {negocio[7]}, '
                        f'Previsão Venda: {negocio[8]}')
            else:
                print("Nenhum negócio encontrado.")

        except (Exception, psycopg2.Error) as e:
            print("Erro ao consultar banco de dados:", e)
        
        finally:
            if connection:
                cursor.close()
                connection.close()


   