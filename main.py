"""
Sistema de Cadastro de Usuários - Console
Autor: Jadson Lago
Descrição: Aplicação em Python para cadastrar, listar e buscar usuários.
"""

# Lista que armazena os usuários em memória
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    idade = input("Idade: ").strip()

    # Validação simples (poderia ser expandida)
    if not nome or not email or not idade.isdigit():
        print("Dados inválidos. Tente novamente.")
        return

    usuario = {
        "nome": nome,
        "email": email,
        "idade": int(idade)
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


# Função principal do sistema
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Buscar Usuário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "4":
            print("Encerrando aplicação.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução principal
if __name__ == "__main__":
    menu()
