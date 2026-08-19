from usuario import *
from menus_e_submenus import menu, limpar_terminal
from menus_e_submenus import limpar_terminal

while True:
	limpar_terminal()
	# Pede usuário e senha
	usuario, senha = tela_de_login()

	# Verifica login e realiza novas tentativas ou cadastro, se necessário
	usuario = cadastrar_ou_tentar_novamente(usuario, senha)

    # Leva ao menu principal caso o login seja realizado
	if usuario:
		limpar_terminal()
		menu(usuario)
