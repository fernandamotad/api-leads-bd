import psycopg2

def conect_db():
    try:
        # Defina as credenciais do banco de dados
        connection = psycopg2.connect(
            host="",  # Endpoint do banco de dados
            database="",    # Nome do banco de dados
            user="postgres",        # Usuário do PostgreSQL
            password="",    # Senha do PostgreSQL
            port="5432"             # Porta do PostgreSQL (padrão 5432)
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao banco de dados:", error)

def inserir_usuario(nivel, nome, login, senha):
  try:
    connection = conect_db()
    cursor = connection.cursor()  

    inserir_sql = ' INSERT INTO usuario (nivel_de_acesso, nome, login, senha) VALUES (%s, %s, %s, %s);'
    cursor.execute(inserir_sql, (nivel, nome, login, senha))
    connection.commit()  # Salva as alterações
    print(f'O usuário {nome} foi cadastrado com sucesso!')
      
  except (Exception, psycopg2.Error) as error:
    print("Erro ao inserir dados:", error)
  finally:
    if connection:
        cursor.close()  
        connection.close()  
def consultar_usuario(login_nome):
    try:
        connection = conect_db()
        cursor = connection.cursor()  
        
        consultar_sql = '''SELECT * 
	FROM usuario WHERE login = %s OR nome = %s;'''
        
        cursor.execute(consultar_sql, (login_nome, login_nome))
        usuario = cursor.fetchone() 
        if usuario:
          nome = usuario[2]
          print(f'Usuário {nome} cadastrado', ) 
        else:
          print(f'Usuário {login_nome} não cadastrado')
    except (Exception, psycopg2.Error) as error:
        print("Erro ao consultar dados:", error)
    finally:
        if connection:
            cursor.close()  
            connection.close()  

# Código de execução
if __name__ == "__main__":
  quantidade = input('Deseja cadastrar quantos usuários? ')
  try:
      quantidade = int(quantidade) 
  except ValueError:
    print("Por favor, insira um número válido.")
  for i in range(1, quantidade + 1): 
    print(f'Digite as informações do {i}° usuário ')
    nivel = input('Digite o nível de acesso: ')
    while True:
      try:
        nivel = int(input('Digite o nível de acesso: '))
        break  
      except ValueError:
        print('O nível de acesso deve ser um número inteiro. Tente novamente.')
    nome = input('Digite o nome: ')
    login = input('Digite o login: ')
    senha = input("Digite a senha: ")
    inserir_usuario(nivel, nome, login, senha)
  print('Usuários Cadastrados')
  
  usuario_consulta = input('Digite o nome de usuario que deseja consultar: ')

  consultar_usuario(str(usuario_consulta))
