
from rich import print
from time import sleep

from informacoes_usuario import *
from usuario import deletar_usuario

# Verifica se uma opção é inteira e está no intervalo correto (Função válida para menus e submenus).
def verificar_opcao(intervalo:int) -> int:
    try:
        opcao = int(input("Escolha uma opção: "))
        while opcao not in range(1, intervalo + 1):  # Abre um loop caso a opção esteja no intervalo incorreto
            print("Digite uma opção no intervalo especificado. Tente novamente!")
            opcao = int(input("Escolha uma opção: "))

        # Animação de carregamento (Só é efetuada se a entrada passar pela checagem)
        print("Carregando", end='')
        for i in range(5):
            print(".", end='')
            sleep(0.3)
        print()

        return opcao
    except ValueError:
        print("[red]Certifique-se de digitar um número inteiro. Tente novamente![/]")
        verificar_opcao()  # Reinicia a verificação se o tipo for incorreto


# Exibe o menu mais hierárquico de opções e recebe o nome do usuário para exibir uma mensagem personalizada.
def menu(usuario):

    while True:
        print(f"\n[bold blue]{' MENU ':=^50}[/]")
        print(f"- O que deseja fazer {usuario}?")
        print("1. Visualizar mapa")
        print("2. Buscar rota")                         #
        print("3. Ver histórico de rotas pesquisadas")
        print("4. Ver rotas favoritas")
        print("5. Informações sobre o usuário")
        print("6. Sair da sessão")
        print(f"[bold blue]{'=' * 50}[/]")

        opcao = verificar_opcao(6)
        
        # Dependendo da entrada, o usuário será direcionado para outra etapa.
        if opcao == 1:
            pass
        elif opcao == 2:
            while True:
                if not submenu_2(usuario):
                    break
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            while True:
                cadastro, info_usuario = exibir_informacoes_usuario(usuario)
                if not submenu_5(cadastro, info_usuario):
                    break
        elif opcao == 6:
            break

def menu_admin():

    while True:
        print(f"\n[bold blue]{' MENU DO ADMIN':=^50}[/]")
        print("1. Ver relatório de uso")
        print("2. Deletar usuário")
        print("3. Sair da sessão")
        print(f"[bold blue]{'=' * 50}[/]")

        opcao = verificar_opcao(3)

        if opcao == 1:
            pass
        elif opcao == 2:
            print('[bold red]ATENÇÂO, essa ação é IRREVERSÍVEL![/]')
            while True:
                nome_usuario = input('Informe o nome do usuário que deseja apagar: ')
                if deletar_usuario(nome_usuario):
                    print(f'Usuário {nome_usuario} deletado com sucesso!')
                    break
                else:
                    escolha = str(input('Usuário não encontrado. Procurar novamente [s/n]?')).strip().lower()
                    if escolha == 's':
                        continue
                    elif escolha == 'n':
                        break

        else:
            break


def submenu_2(usuario) -> int:
    
    print(
        f'\n[bold blue]{' BUSCAR ROTA ':=^40}[/]\n'
        '- Digite o número para realizar tal ação:\n'
        '1 - Criar nova rota\n'
        '2 - Selecionar dentre rotas Favoritas\n'
        '3 - Selecionar dentre rotas no Histórico\n' 
        '4 - Voltar\n'
        f'[bold blue]{'=' * 40}[/]'     
    )

    opcao = verificar_opcao(4)

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    else:
        return False


def submenu_5(cadastro, info_usuario):

    print(f"\n[bold blue]{' AÇÕES ':=^40}[/]")
    print("1. Limpar Histórico")
    print("2. Redefinir senha")                         #
    print("3. Excluir conta")
    print("4. Voltar")
    print(f"[bold blue]{'=' * 40}[/]")

    opcao = verificar_opcao(4)

    if opcao == 1:
        pass
    elif opcao == 2:
        redefinir_senha(cadastro, info_usuario)
    elif opcao == 3:
        pass
    elif opcao == 4:
        return False