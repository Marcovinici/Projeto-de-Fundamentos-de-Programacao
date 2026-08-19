from usuario import *
from menus_e_submenus import menu
import os

def limpar_terminal():
    """
    Limpa a tela do terminal independentemente do sistema operacional.
    """
    # 'nt' significa Windows, caso contrário assume Unix (Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
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
