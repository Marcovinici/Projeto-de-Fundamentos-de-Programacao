from usuario import *
from menus_e_submenus import menu, menu_admin, limpar_terminal

while True:
	limpar_terminal()
	print(f"\n[bold blue]{' BEM VINDO AO MOBCLI ':=^50}[/]")
	print('Por favor, insira suas credenciais.')
	# Pede usuário e senha
	usuario, senha = tela_de_login()

	# Verifica login e realiza novas tentativas ou cadastro, se necessário
	usuario = cadastrar_ou_tentar_novamente(usuario, senha)

    # Leva ao menu principal ou ao menu do admin caso o login seja realizado
	if usuario:
		limpar_terminal()
		cadastro = carregar_cadastro()
		if usuario == 'admin' and cadastro.get('admin')['senha'] == senha:
			menu_admin()
		else:
			menu(usuario)
