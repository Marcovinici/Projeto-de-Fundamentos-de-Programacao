from usuario import *
from menus_e_submenus import menu

while True:
    # Pede usuário e senha
    usuario, senha = tela_de_login()

    # Verifica login e realiza novas tentativas ou cadastro, se necessário
    usuario = cadastrar_ou_tentar_novamente(usuario, senha)

    # Leva ao menu principal caso o login seja realizado
    if usuario:
        menu(usuario)