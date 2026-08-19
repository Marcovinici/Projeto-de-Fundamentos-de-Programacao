import json
from time import sleep
from datetime import date
from rich import print

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
        # Solicita usuário e senha na cor azul
        usuario = input("\033[1;34mUsuário: \033[m")
        senha = input("\033[1;34mSenha: \033[m")
    # Trata exceções, como interrupção do teclado (Ctrl+C) e entradas inválidas.
    except KeyboardInterrupt:
        print("\n[bold red]Operação cancelada pelo usuário.[/]")
        exit()
    if not usuario or not senha or " " in usuario or " " in senha:
        print("[bold red]Usuário e senha não podem ser vazios ou conter espaços.[/]")
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
        # Verifica se a senha está incorreta para um usuário existente.
        if usuario in carregar_cadastro():
            print("[bold red]Senha incorreta. Tente novamente.[/]")
            usuario, senha = tela_de_login()
            return cadastrar_ou_tentar_novamente(usuario, senha)
        print("[bold red]Usuário não encontrado.[/] Cadastrar novo usuário? (s/n)")
        resposta = input().lower()
        if resposta == "s":
            # Se a resposta for sim, cadastra o novo usuário e retorna ao menu.
            # Mostra uma animação de carregamento para o usuário.
            print("Cadastrando novo usuário", end='')
            for i in range(1, 4):
                print(".", end='')
                sleep(0.5)
            print("\n[bold green]Usuário cadastrado com sucesso![/]")
            # Registra o novo usuário no banco de dados e retorna o usuário para o menu principal.
            cadastrar_usuario(usuario, senha)
            return usuario
        else:
            # Se a resposta não for "s", solicita novamente o login.
            print("[bold red]Tente novamente.[/]")
            usuario, senha = tela_de_login()
            return cadastrar_ou_tentar_novamente(usuario, senha)
    else:
        # Retorna o usuário caso o login seja bem-sucedido.
        print("\n[bold green]Login bem-sucedido![/]")
        return usuario


def cadastrar_usuario(usuario, senha):
    # Carrega o banco de dados, adiciona o novo usuário e salva as alterações.
    cadastro = carregar_cadastro()
    cadastro[usuario] = {
        "senha": senha,
        "data": date.today().strftime("%d/%m/%Y"),
        "historico": [

        ],
        "favoritos": [

        ]
    }
    # Adiciona no usuário sua senha, data de criação, histórico e rotas favoritas.
    with open('banco_de_dados.json', 'w') as arquivo:
        json.dump(cadastro, arquivo, indent=4)


def deletar_usuario(usuario):
    cadastro = carregar_cadastro()
    if usuario in cadastro:
        del cadastro[usuario]
        with open('banco_de_dados.json', 'w') as arquivo:
            json.dump(cadastro, arquivo, indent=4)
        return True
    else:
        return False
        