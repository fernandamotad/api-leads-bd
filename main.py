import psycopg2, os
from dotenv import load_dotenv
from db import Database
from usuario import Usuario
from lead import Lead
from negocio import Negocio

def menu():
    """Exibe o menu principal e redireciona para a opção escolhida."""
    while True:
        print("\n--- Menu Principal ---")
        print("1. Ir para Menu Lead")
        print("2. Ir para Menu Usuário")
        print("3. Ir para Menu Negócio")
        print("4. Sair")

        try:
            escolha = int(input("Escolha uma opção (1-4): "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if escolha == 1:
            menu_lead()
        elif escolha == 2:
            menu_usuario()
        elif escolha == 3:
            menu_negocio()
        elif escolha == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_lead():
    """Menu para consultar ou inserir Leads."""
    lead_service = Lead(db)
    
    print("\n--- Menu Lead ---")
    print("1. Inserir Lead")
    print("2. Consultar Lead")
    print("3. Listar todos os Leads")
    
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        nome = input("Digite o nome do lead: ")
        telefone = input("Digite o telefone do lead: ")
        telefone_adicional = input("Digite o telefone adicional (opcional): ") or None
        email = input("Digite o email (opcional): ") or None
        anotacao = input("Digite uma anotação (opcional): ") or None
        lead_service.inserir_lead(nome, telefone, telefone_adicional, email, anotacao)
    elif escolha == 2:
        lead_consulta = input("Digite o nome ou telefone do lead: ")
        lead_service.consultar_lead(lead_consulta)
    elif escolha == 3:
        lead_service.listar_todos_leads()
    else:
        print("Opção inválida.")

def menu_usuario():
    """Menu para consultar ou inserir Usuários."""
    usuario_service = Usuario(db)

    print("\n--- Menu Usuário ---")
    print("1. Inserir Usuário")
    print("2. Consultar Usuário")
    print("3. Listar todos os Usuários")
    
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        nivel = int(input("Digite o nível de acesso: "))
        nome = input("Digite o nome: ")
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        usuario_service.inserir_usuario(nivel, nome, login, senha)
    elif escolha == 2:
        usuario_consulta = input("Digite o nome ou login do usuário: ")
        usuario_service.consultar_usuario(usuario_consulta)
    elif escolha == 3:
        usuario_service.listar_todos_usuarios()
    else:
        print("Opção inválida.")

def menu_negocio():
    """Menu para consultar ou inserir Negócios."""
    negocio_service = Negocio(db)
    
    print("\n--- Menu Negócio ---")
    print("1. Inserir Negócio")
    print("2. Consultar Negócio")
    print("3. Listar Todos os Negócios")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        titulo = input("Digite o título do negócio: ")
        vencimento_atualizacao = input("Digite a data limite da próxima atualização no formato dd/mm/aaaa: ")
        idlead = input("Digite o ID do lead: ")
        etapa = input("Digite a etapa do negócio: ")
        idusuario = input("Digite o ID do usuário responsável: ")
        descricao = input("Digite a descrição (opcional): ") or None
        previsao_venda = input("Digite a previsão de venda (opcional): ") or None
        negocio_service.inserir_negocio(
            titulo, vencimento_atualizacao, 
            idlead, etapa, idusuario, 
            descricao, previsao_venda)
        

    elif escolha == 2:
        consulta_negocio = input("Digite o título ou ID do negócio: ")
        negocio_service.consultar_negocio(consulta_negocio)
    
    elif escolha == 3:
        negocio_service.listar_todos_negocios()
   
    else:
        print("Opção inválida.")

def main():
    """Função principal que inicializa o banco de dados e executa o menu."""
    global db
    load_dotenv()
    try:
        # Inicializa o banco de dados
        db = Database (
            host = os.getenv('host'),
            database = "Multiple-lead",
            user = os.getenv('user'),
            password = os.getenv('password'),
            port = '5432'
        )
        # Executa o menu principal
        menu()
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# Executar o programa
if __name__ == "__main__":
    main()