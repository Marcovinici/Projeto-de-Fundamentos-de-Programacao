from rich import print
from time import sleep
import os
from selecionar_rota import selecionar_rota

from informacoes_usuario import *
from usuario import deletar_usuario
from relatorio import exibir_relatorio
from historico import apagar_historico, mostrar_historico
from favoritos import apagar_favoritos, mostrar_favoritos, carregar_dados
from busca import mapa_principal, buscar, imprimir_mapa_colorido_text



def limpar_terminal():
    """
    Limpa a tela do terminal independentemente do sistema operacional.
    """
    # 'nt' significa Windows, caso contrário assume Unix (Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')


def voltar():
    while True:
        try:
            escolha = int(input('Digite 0 para voltar: '))

            if escolha == 0:
                break
            else:
                print('[bold red]Certifique-se de digitar 0.[/]')

        except ValueError:
            print('[bold red]Certifique-se de digitar o número 0![/]')


def verificar_opcao(intervalo: int) -> int:
    """
    Solicita e verifica uma opção após exibir um menu ou submenu qualquer.
    A verificação ocorre com base no intervalo de opções disponíveis do menu.

    Args:
        intervalo (int): número de opções do menu ou submenu.

    Returns:
        int: opção escolhida pelo usuário.
    """
    try:
        opcao = int(input("Escolha uma opção: "))

        while opcao not in range(1, intervalo + 1):
            print("Digite uma opção no intervalo especificado. Tente novamente!")
            opcao = int(input("Escolha uma opção: "))

        limpar_terminal()

        return opcao

    except ValueError:
        print("[red]Certifique-se de digitar um número inteiro. Tente novamente![/]")
        return verificar_opcao(intervalo)


def menu(usuario):
    """
    Exibe um menu de opções para o usuário iniciar a interação com o sistema.

    Args:
        usuario (string): nome do usuário tal qual como foi cadastrado.
    """
    while True:

        # Caso o usuário não esteja mais presente no banco de dados,
        # ele será informado e retornará para a tela de login.
        cadastro = carregar_cadastro()

        if usuario not in cadastro:
            print(
                f"[bold red]Usuário {usuario} não encontrado. "
                "Faça login novamente.[/]"
            )
            break

        limpar_terminal()

        print(f"\n[bold blue]{' MENU ':=^50}[/]")
        print(f"- O que deseja fazer {usuario}?")
        print("1. Visualizar mapa")
        print("2. Buscar rota")
        print("3. Ver histórico de rotas")
        print("4. Ver rotas favoritas")
        print("5. Informações sobre o usuário")
        print("6. Sair da sessão")
        print(f"[bold blue]{'=' * 50}[/]")

        opcao = verificar_opcao(6)

        # Dependendo da entrada, o usuário será direcionado para outra etapa.
        if opcao == 1:
            mapa_principal()
            imprimir_mapa_colorido_text("mapa_principal")
            voltar()

        elif opcao == 2:
            while True:
                if not submenu_2(usuario):
                    break

        elif opcao == 3:
            mostrar_historico(usuario)
            voltar()

        elif opcao == 4:
            mostrar_favoritos(usuario)
            voltar()

        elif opcao == 5:
            deslogar = False

            while True:
                cadastro, info_usuario = exibir_informacoes_usuario(usuario)
                resultado = submenu_5(cadastro, info_usuario, usuario)

                if resultado == "LOGOUT":
                    deslogar = True
                    break

                elif not resultado:
                    break

            if deslogar:
                break

        elif opcao == 6:
            break


def menu_admin():
    """
    Exibe um menu interativo reduzido para indivíduos que fazem login
    como administrador.
    """
    while True:
        limpar_terminal()

        print(f"\n[bold blue]{' MENU DO ADMIN':=^50}[/]")
        print("1. Ver relatório de uso")
        print("2. Deletar usuário")
        print("3. Sair da sessão")
        print(f"[bold blue]{'=' * 50}[/]")

        opcao = verificar_opcao(3)

        if opcao == 1:
            exibir_relatorio()
            voltar()

        elif opcao == 2:
            print('[bold red]ATENÇÂO, essa ação é IRREVERSÍVEL![/]')

            while True:
                nome_usuario = input(
                    'Informe o nome do usuário que deseja apagar: '
                )

                if deletar_usuario(nome_usuario):
                    print(
                        f'Usuário {nome_usuario} deletado com sucesso!'
                    )
                    break

                else:
                    escolha = str(
                        input(
                            'Usuário não encontrado. '
                            'Procurar novamente [s/n]?'
                        )
                    ).strip().lower()

                    if escolha == 's':
                        continue

                    elif escolha == 'n':
                        break

        else:
            break


def submenu_2(usuario) -> int:
    """
    Exibe um submenu interativo caso o usuário escolha a opção 2
    do menu principal.

    Returns:
        False se o usuário desejar voltar ao menu principal.
    """
    limpar_terminal()

    print(
        f'\n[bold blue]{' BUSCAR ROTA ':=^40}[/]\n'
        '- Digite o número para realizar tal ação:\n'
        '1 - Criar nova rota\n'
        '2 - Escolher de favoritos\n'
        '3 - Escolher de histórico\n'
        '4 - Voltar\n'
        f'[bold blue]{'=' * 40}[/]'
    )

    opcao = verificar_opcao(4)

    if opcao == 1:
        print(
            f'\n[bold blue]{' CRIAR ROTA ':=^40}[/]\n'
            "F. Fazenda Lama Podre\n"
            "R. Rodoviária de Juazeiro do Norte\n"
            "H. Horto do Padre Cícero\n"
            "S. Sítio Fundão\n"
            "P. Parque das Timbaúbas\n"
            "E. Estádio Romeirão\n"
            "I. Instituto Federal\n"
            f'[bold blue]{'=' * 40}[/]'
        )

        rota = selecionar_rota(
            ["F", "R", "H", "S", "P", "E", "I"],
            usuario
        )

        if rota:
            buscar(rota)

        voltar()

    elif opcao == 2:
        menu_favoritos(usuario)
        voltar()

    elif opcao == 3:
        menu_historico(usuario)
        voltar()
    else:
        return False


def submenu_5(cadastro, info_usuario, usuario):
    """
    Exibe um submenu interativo caso o usuário escolha a opção 5
    do menu principal.

    Returns:
        False se o usuário desejar voltar ao menu principal,
        ou "LOGOUT" se a conta for excluída.
    """
    print(f"\n[bold blue]{' AÇÕES ':=^40}[/]")
    print("1. Limpar histórico")
    print("2. Limpar favoritos")
    print("3. Redefinir senha")
    print("4. Excluir conta")
    print("5. Voltar")
    print(f"[bold blue]{'=' * 40}[/]")

    opcao = verificar_opcao(5)

    if opcao == 1:

        while True:
            confirmacao = input(
                "Deseja confirmar a exclusão do seu histórico? (s/n): "
            ).strip().lower()

            if confirmacao == "s":
                apagar_historico(usuario)
                print("[bold green]Histórico excluído com sucesso![/]")
                return "LOGOUT"

            elif confirmacao == "n":
                print("Exclusão cancelada.")
                break

            else:
                print(
                    "[bold red]Opção inválida. Para excluir o histórico, "
                    "digite 's' para sim ou 'n' para não.[/]"
                )

    elif opcao == 2:

        while True:
            confirmacao = input(
                "Deseja confirmar a exclusão dos seus favoritos? (s/n): "
            ).strip().lower()

            if confirmacao == "s":
                apagar_favoritos(usuario)
                print("[bold green]Favoritos excluídos com sucesso![/]")
                return "LOGOUT"

            elif confirmacao == "n":
                print("Exclusão cancelada.")
                break

            else:
                print(
                    "[bold red]Opção inválida. Para excluir favoritos, "
                    "digite 's' para sim ou 'n' para não.[/]"
                )

    elif opcao == 3:

        while True:
            confirmacao = input(
                "Deseja continuar com a redefinição de senha? (s/n): "
            ).strip().lower()

            if confirmacao == "s":
                redefinir_senha(cadastro, info_usuario)
                print("[bold green]Senha redefinida com sucesso![/]")
                return "LOGOUT"

            elif confirmacao == "n":
                print("Operação cancelada.")
                break

            else:
                print(
                    "[bold red]Opção inválida. Para redefinir senha, "
                    "digite 's' para sim ou 'n' para não.[/]"
                )

    elif opcao == 4:
        deletar_usuario(usuario)
        return False

    elif opcao == 5:
        return False


def menu_favoritos(usuario):

    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return submenu_2(usuario)

    favoritos = dados[usuario].get("favoritos", [])

    if not favoritos:
        print("Você não possui rotas favoritas.")
        return submenu_2(usuario)

    print(
        f"\n[bold blue]{' ========== ROTAS FAVORITAS ========== ':=^40}[/]"
    )

    for i, favorito in enumerate(favoritos, start=1):
        rota = favorito["rota"]
        print(f"{i} - {rota[0]} → {rota[1]}")

    print("0 - Voltar")

    while True:
        try:
            escolha = int(
                input("\nDigite o número da rota que deseja usar: ")
            )

            if escolha == 0:
                return submenu_2(usuario)

            if 1 <= escolha <= len(favoritos):
                return buscar(
                    favoritos[escolha - 1]["rota"]
                )

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas um número.")


def menu_historico(usuario):

    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return submenu_2(usuario)

    historico = dados[usuario].get("historico", [])

    if not historico:
        print("Você não possui rotas no histórico.")
        return submenu_2(usuario)

    print("\n========== HISTÓRICO DE ROTAS ==========")

    for i, registro in enumerate(historico, start=1):
        rota = registro["rota"]
        data = registro["data"]

        print(f"{i} - {rota[0]} → {rota[1]} | {data}")

    print("0 - Voltar")

    while True:
        try:
            escolha = int(
                input("\nDigite o número da rota que deseja usar: ")
            )

            if escolha == 0:
                return submenu_2(usuario)

            if 1 <= escolha <= len(historico):
                return buscar(
                    historico[escolha - 1]["rota"]
                )

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas um número.")