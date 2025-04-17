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

def solicitar_input(mensagem: str, validacao: callable = None, erro: str = None) -> str:
    """Solicita e valida uma entrada do usuário."""
    while True:
        entrada = input(mensagem).strip()
        if validacao and not validacao(entrada):
            print(erro or "❌ Entrada inválida.")
        else:
            return entrada

def solicitar_nome() -> str:
    """Solicita e valida o nome do usuário."""
    return solicitar_input(
        "Nome: ",
        validacao=lambda nome: nome and not nome.replace(" ", "").isdigit(),
        erro="❌ Erro: O nome não pode estar vazio ou conter apenas números."
    )

def solicitar_email() -> str:
    """Solicita e valida o e-mail do usuário."""
    return solicitar_input(
        "E-mail: ",
        validacao=validar_email,
        erro="❌ Erro: O e-mail deve conter '@' e '.' (exemplo: usuario@provedor.com)."
    )

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
    detalhes = f"  Nome: {usuario['nome']} | E-mail: {usuario['email']} | Idade: {usuario['idade']}"
    if com_indice and indice:
        print(f"\nUsuário {indice}:\n{detalhes}")
    else:
        print(detalhes)

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
    opcoes = {
        "1": cadastrar_usuario,
        "2": listar_usuarios,
        "3": buscar_usuario,
        "4": lambda: print(MSG_SAINDO) or exit()
    }
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        acao = opcoes.get(opcao, lambda: print(MSG_OPCAO_INVALIDA))
        acao()

# Inicialização do sistema
if __name__ == "__main__":
    executar()