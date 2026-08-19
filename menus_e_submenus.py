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

def verificar_opcao(intervalo:int) -> int:
    """
    Solicita e verifica uma opção após exibir um menu ou submenu qualquer. A verificação ocorre com base no intervalo de opções disponíveis do menu.

    Args:
        intervalo (int): é o número de opções do menu ou submenu

    Return:
        opcao (int): a opção escolhida pelo usuário

    Raises:
        ValueError: se a opção não for um número inteiro
    """
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
        limpar_terminal()

        return opcao
    except ValueError:
        print("[red]Certifique-se de digitar um número inteiro. Tente novamente![/]")
        verificar_opcao()  # Reinicia a verificação se o tipo for incorreto


def menu(usuario):
    """
    Exibe um menu de opções para o usuário iniciar a interação com o sistema, bem como uma mensagem personalizada com seu nome.

    Args:
        usuario (string): O nome do usuário tal qual como foi cadastrado
    """
    while True:
        # Caso o usuário não esteja mais presente no banco de dados, ele será informado e retornará para a tela de login.
        cadastro = carregar_cadastro()
        if usuario not in cadastro:
            print(f"[bold red]Usuário {usuario} não encontrado. Faça login novamente.[/]")
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
            while True:
                cadastro, info_usuario = exibir_informacoes_usuario(usuario)
                if not submenu_5(cadastro, info_usuario, usuario):
                    break
        elif opcao == 6:
            break


def menu_admin():
    """
    Exibe um menu interativo reduzido para indivíduos que fazem login como administrador
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
    """
    Exibe um submenu interativo caso o usuário escolha a opção 2 do menu principal (buscar rota)

    Args:
        usuario (string): nome do usuario tal qual como foi cadastrado
    
    Returns:
        False se o usuário desejar voltar ao menu principal
    """
    limpar_terminal()
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
        print(f'\n[bold blue]{' CRIAR ROTA ':=^40}[/]\n'
            "F. Fazenda Lama Podre\n"
            "R. Rodoviária de Juazeiro do Norte\n"
            "H. Horto do Padre Cícero\n"
            "S. Sítio Fundão\n"
            "P. Parque das Timbaúbas\n"
            "E. Estádio Romeirão\n"
            "I. Instituto Federal\n"
            f'[bold blue]{'=' * 40}[/]'
        )
        rota = selecionar_rota(["F" ,"R", "H", "S", "P", "E", "I"], usuario)
        if rota:
            buscar(rota)
            imprimir_mapa_colorido_text("novo_mapa.txt")
        voltar()
    elif opcao == 2:
        return menu_favoritos(usuario)
        
    elif opcao == 3:
        return menu_historico(usuario)     
    else:
        return False


def submenu_5(cadastro, info_usuario, usuario):
    """
    Exibe um submenu interativo caso o usuário escolha a opção 5 do menu principal (informações do usuário)

    Args:
        cadastro: chama a função que carrega o banco de dados
        info_usuario (dict): dicionário com os dados do usuário (como senha, data, historico e favoritos)
        usuario (string): nome do usuario tal qual como foi cadastrado

    Returns:
        False se o usuário desejar voltar ao menu principal

    """

    print(f"\n[bold blue]{' AÇÕES ':=^40}[/]")
    print("1. Limpar histórico")
    print("2. Limpar favoritos")
    print("3. Redefinir senha")                         #
    print("4. Excluir conta")
    print("5. Voltar")
    print(f"[bold blue]{'=' * 40}[/]")

    opcao = verificar_opcao(5)

    if opcao == 1:
        apagar_historico(usuario)
    elif opcao == 2:
        apagar_favoritos(usuario)
    elif opcao == 3:
        redefinir_senha(cadastro, info_usuario)
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

    
    print(f"\n[bold blue]{' ========== ROTAS FAVORITAS ========== ':=^40}[/]")

    for i, favorito in enumerate(favoritos, start=1):
        rota = favorito["rota"]
        print(f"{i} - {rota[0]} → {rota[1]}")

    print("0 - Voltar")

    while True:
        try:
            escolha = int(input("\nDigite o número da rota que deseja usar: "))

            if escolha == 0:
                return submenu_2(usuario)

            if 1 <= escolha <= len(favoritos):
                return buscar(favoritos[escolha - 1]["rota"])

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas um número.")

def menu_historico(usuario):

    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return submenu_2

    historico = dados[usuario].get("historico", [])

    if not historico:
        print("Você não possui rotas no histórico.")
        return submenu_2

    print("\n========== HISTÓRICO DE ROTAS ==========")

    for i, registro in enumerate(historico, start=1):
        rota = registro["rota"]
        data = registro["data"]

        print(f"{i} - {rota[0]} → {rota[1]} | {data}")

    print("0 - Voltar")

    while True:
        try:
            escolha = int(input("\nDigite o número da rota que deseja usar: "))

            if escolha == 0:
                return submenu_2

            if 1 <= escolha <= len(historico):
                return buscar(historico[escolha - 1]["rota"])

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas um número.")

