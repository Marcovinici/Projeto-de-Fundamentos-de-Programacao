import json
from time import sleep
from menu_principal import menu

# Abre ou cria o banco de dados caso não exista
def carregar_cadastro():
    try:
        with open('banco_de_dados.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def tela_de_login():
    # Cria a tela de login e recebe usuario e senha.
    try:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
    # Trata exceções, como interrupção do teclado (Ctrl+C) e entradas inválidas.
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit()
    if not usuario or not senha or " " in usuario or " " in senha:
        print("Usuário e senha não podem ser vazios ou conter espaços.")
        return tela_de_login()
    # Retorna o usuário e a senha para a função que chamou.
    return usuario, senha
        
def verificar_usuario(usuario, senha):
    # Carrega o banco de dados.
    cadastro = carregar_cadastro()
    # Verifica se o usuário existe e se a senha está correta. Caso contrário, retorna False.
    return usuario in cadastro and cadastro[usuario]["senha"] == senha

def cadastrar_ou_tentar_novamente(usuario, senha):
    # Se o usuário não for encontrado, oferece a opção de cadastrar um novo usuário.
    if not verificar_usuario(usuario, senha):
        print("Usuário não encontrado. Cadastrar novo usuário? (s/n)")
        resposta = input().lower()
        if resposta == "s":
            # Se a resposta for sim, cadastra o novo usuário e retorna ao menu.
            # Mostra uma animação de carregamento para o usuário.
            for i in range(1, 4):
                print(f"Cadastrando novo usuários {"." * i}")
                sleep(0.5)
            print("Usuário cadastrado com sucesso!")
            # Leva o usuário ao menu principal após o cadastro.
            cadastrar_usuario(usuario, senha)
            return menu(usuario)
        else:
            # Se a resposta não for "s", solicita novamente o login.
            print("Tente novamente.")
            usuario, senha = tela_de_login()
            cadastrar_ou_tentar_novamente(usuario, senha)
    else:
        # Leva ao menu principal caso o usuário seja encontrado e a senha esteja correta.
        print("Login bem-sucedido!")
        return menu(usuario)

def cadastrar_usuario(usuario, senha):
    # Carrega o banco de dados, adiciona o novo usuário e salva as alterações.
    cadastro = carregar_cadastro()
    cadastro[usuario] = {
        "senha": senha
    }
    with open('banco_de_dados.json', 'w') as arquivo:
        json.dump(cadastro, arquivo, indent=4)
