"""
Sistema de Cadastro de Usuários - Console
Autor: Jadson Lago
Descrição: Aplicação em Python para cadastrar, listar (com paginação) e buscar usuários.
"""

# Constantes para mensagens
MSG_CABECALHO = "\n" + "=" * 30
MSG_MENU = "MENU PRINCIPAL"
MSG_OPCAO_INVALIDA = "❌ Opção inválida. Tente novamente."
MSG_SUCESSO_CADASTRO = "✅ Usuário cadastrado com sucesso!"
MSG_SAINDO = "\nSaindo do sistema..."

# Lista em memória para armazenar usuários
usuarios = []

# --------------------------------------------
# Validações e Entradas de Dados
# --------------------------------------------
def validar_email(email: str) -> bool:
    """Verifica se o e-mail contém '@' e '.'."""
    return '@' in email and '.' in email

def solicitar_nome() -> str:
    """Solicita e valida o nome do usuário."""
    while True:
        nome = input("Nome: ").strip()
        if not nome:
            print("❌ Erro: O nome não pode estar vazio.")
        elif nome.replace(" ", "").isdigit():
            print("❌ Erro: O nome não pode conter apenas números.")
        else:
            return nome

def solicitar_email() -> str:
    """Solicita e valida o e-mail do usuário."""
    while True:
        email = input("E-mail: ").strip()
        if validar_email(email):
            return email
        print("❌ Erro: O e-mail deve conter '@' e '.' (exemplo: usuario@provedor.com).")

def solicitar_idade() -> int:
    """Solicita e valida a idade do usuário."""
    while True:
        try:
            return int(input("Idade: ").strip())
        except ValueError:
            print("❌ Erro: A idade deve ser um número inteiro.")

# --------------------------------------------
# Funcionalidades do Sistema
# --------------------------------------------
def cadastrar_usuario():
    """Realiza o cadastro de um novo usuário."""
    print("\nCadastro de Usuário")
    usuarios.append({
        "nome": solicitar_nome(),
        "email": solicitar_email(),
        "idade": solicitar_idade()
    })
    print(MSG_SUCESSO_CADASTRO)

def exibir_usuario(usuario: dict, com_indice: bool = False, indice: int = None):
    """Exibe os detalhes de um usuário formatados."""
    if com_indice and indice:
        print(f"\nUsuário {indice}:")
        print(f"  Nome: {usuario['nome']}")
        print(f"  E-mail: {usuario['email']}")
        print(f"  Idade: {usuario['idade']}")
    else:
        print(f"  Nome: {usuario['nome']} | E-mail: {usuario['email']} | Idade: {usuario['idade']}")

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    print("\nLista de Usuários:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for indice, usuario in enumerate(usuarios, 1):
        exibir_usuario(usuario, com_indice=True, indice=indice)

def buscar_usuario():
    """Busca usuários por nome (parcial e case-insensitive)."""
    termo = input("\nDigite o nome para busca: ").strip().lower()
    resultados = [u for u in usuarios if termo in u["nome"].lower()]
    
    print(f"\n🔍 Resultados para '{termo}':")
    if not resultados:
        print("Nenhum usuário encontrado.")
    else:
        for usuario in resultados:
            exibir_usuario(usuario)

# --------------------------------------------
# Controle do Menu
# --------------------------------------------
def exibir_menu():
    """Exibe o menu principal formatado."""
    print(MSG_CABECALHO)
    print(MSG_MENU)
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário por nome")
    print("4. Sair")

def executar():
    """Controla o fluxo principal da aplicação."""
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        match opcao:
            case "1": cadastrar_usuario()
            case "2": listar_usuarios()
            case "3": buscar_usuario()
            case "4": 
                print(MSG_SAINDO)
                break
            case _: print(MSG_OPCAO_INVALIDA)

# Inicialização do sistema
if __name__ == "__main__":
    executar()