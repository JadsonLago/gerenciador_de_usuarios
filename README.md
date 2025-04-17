# Sistema de Cadastro de Usuários

![CLI](https://img.shields.io/badge/Interface-CLI-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-green)

Um sistema de cadastro de usuários via linha de comando (CLI) com validações e armazenamento em memória.

## Funcionalidades

- **Cadastro de usuários**  
  Validações para:
  - Nome (não pode ser vazio ou conter apenas números)
  - E-mail (formato básico com `@` e `.`)
  - Idade (deve ser um número inteiro)
- **Listagem completa de usuários**
- **Busca por nome** (parcial e sem distinção de maiúsculas/minúsculas)
- **Cadastro múltiplo** em sequência
- Menu interativo

## Pré-requisitos

- Python 3.10 ou superior

## Como Executar

1. Baixe o arquivo `cadastro_usuarios.py`
2. No terminal, navegue até o diretório do arquivo
3. Execute o comando:
   ```bash
   python cadastro_usuarios.py  
   
Código modularizado com separação de responsabilidades

Mensagens intuitivas para orientar o usuário

Armazenamento em memória (os dados são resetados ao fechar o programa)