"""
Sistema de Cadastro de Usuários - Console
Autor: Jadson Lago
Descrição: Aplicação em Python para cadastrar, listar (com paginação) e buscar usuários.
"""
# Sistema de Cadastro de Usuários

# Lista em memória para armazenar os usuários
usuarios = []

def cadastrar_usuario():
    """Cadastra um novo usuário solicitando nome, e-mail e idade."""
    print("\nCadastro de Usuário")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    
    # Validação da idade (deve ser um número inteiro)
    while True:
        idade = input("Idade: ").strip()
        try:
            idade = int(idade)
            break
        except ValueError:
            print("Erro: A idade deve ser um número inteiro. Tente novamente.")
    
    # Adiciona o usuário à lista
    usuarios.append({"nome": nome, "email": email, "idade": idade})
    print("✅ Usuário cadastrado com sucesso!")


def listar_usuarios():
    """Lista todos os usuários cadastrados no console."""
    print("\nLista de Usuários:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    # Exibe os detalhes de cada usuário
    for indice, usuario in enumerate(usuarios, 1):
        print(f"\nUsuário {indice}:")
        print(f"  Nome: {usuario['nome']}")
        print(f"  E-mail: {usuario['email']}")
        print(f"  Idade: {usuario['idade']}")


def buscar_usuario():
    """Busca usuários pelo nome (case-insensitive e parcial)."""
    termo = input("\nDigite o nome para busca: ").strip().lower()
    resultados = []
    
    for usuario in usuarios:
        # Verifica se o termo está contido no nome (ignorando maiúsculas/minúsculas)
        if termo in usuario["nome"].lower():
            resultados.append(usuario)
    
    # Exibe os resultados
    print(f"\n🔍 Resultados para '{termo}':")
    if not resultados:
        print("Nenhum usuário encontrado.")
    else:
        for usuario in resultados:
            print(f"  Nome: {usuario['nome']} | E-mail: {usuario['email']} | Idade: {usuario['idade']}")


# Menu principal
while True:
    print("\n" + "=" * 30)
    print("MENU PRINCIPAL")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        buscar_usuario()
    elif opcao == "4":
        print("\nSaindo do sistema...")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")