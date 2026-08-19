<<<<<<< HEAD
from usuario import tela_de_login, cadastrar_ou_tentar_novamente
from menus_e_submenus import menu, limpar_terminal

=======
from usuario import *
from menus_e_submenus import menu, menu_admin, limpar_terminal

while True:
	limpar_terminal()
	print(f"\n[bold blue]{' BEM VINDO AO MOBCLI ':=^50}[/]")
	print('Por favor, insira suas credenciais.')
	# Pede usuário e senha
	usuario, senha = tela_de_login()
>>>>>>> 0b5c59d915d46e1dd2424be4ddaa5a9030632903

def main():
    while True:
        limpar_terminal()

        # Pede usuário e senha
        usuario, senha = tela_de_login()

        # Verifica login e realiza novas tentativas ou cadastro
        usuario = cadastrar_ou_tentar_novamente(usuario, senha)

        # Leva ao menu principal caso o login seja realizado
        if usuario:
            limpar_terminal()
            menu(usuario)


if __name__ == "__main__":
    main()
