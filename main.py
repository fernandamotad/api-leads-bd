import psycopg2
from db import Database
from usuario import Usuario
from lead import Lead

if __name__ == "__main__":
    # Inicializa o banco de dados
    db = Database(
        host="database-1.c8v407oicw0t.us-east-1.rds.amazonaws.com",     # Endpoint do banco de dados 
        database="Multiple-lead",          # Nome do banco de dados
        user="postgres",      # Usuário do banco
        password="88778159"  # Senha do banco
    )




    usuario_service = Usuario(db)
    
    print("Vamos cadastrar usuários ao sistema")    
    quantidade = input('Deseja cadastrar quantos usuários? ')
    try:
        quantidade = int(quantidade)
    except ValueError:
        print("Por favor, insira um número válido.")
    
    for i in range(1, quantidade + 1):
        print(f'Digite as informações do {i}° usuário ')
        while True:
            try:
                nivel = int(input('Digite o nível de acesso: '))
                break
            except ValueError:
                print('O nível de acesso deve ser um número inteiro. Tente novamente.')
        nome = input('Digite o nome: ')
        login = input('Digite o login: ')
        senha = input("Digite a senha: ")
        usuario_service.inserir_usuario(nivel, nome, login, senha)

    usuario_consulta = input('Digite o nome ou login do usuário que deseja consultar: ')
    usuario_service.consultar_usuario(usuario_consulta)





    lead_service = Lead(db)

    # Exemplo de inserção de lead
    print("Agora vamos cadastrar um lead ao sistema")
    nome = input("Digite o nome do lead: ")
    telefone = input("Digite o telefone do lead: ")

    telefone_adicional = input("Digite o telefone adicional do lead (opcional): ") or None
    email = input("Digite o email do lead (opcional): ") or None
    anotacao = input("Digite uma anotação (opcional): ") or None
    
    lead_service.inserir_lead(nome, telefone, telefone_adicional, email, anotacao)

    # Exemplo de consulta de lead
    lead_consulta = input("Digite o nome ou telefone do lead para consultar: ")
    lead_service.consultar_lead(lead_consulta)

    # Exemplo de listar todos os leads
    lead_service.listar_todos_leads()