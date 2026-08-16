# Exemplo de menu principal
# É uma gama de opções que aparece após o usuário efetuar o login ou se cadastrar no sistema

# Kauê Aparecido 14/08

from rich import print
from time import sleep
from informacoes_usuario import *

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

    print(f"\n[bold blue]{' MENU ':=^40}[/]")
    print(f"- O que deseja fazer {usuario}?")
    print("1. Visualizar mapa")
    print("2. Buscar rota")                         #
    print("3. Ver histórico de rotas pesquisadas")
    print("4. Ver rotas favoritas")
    print("5. Informações sobre o usuário")
    print("6. Sair da sessão")
    print(f"[bold blue]{'=' * 40}[/]")

    opcao = verificar_opcao(6)
    
    # Dependendo da entrada, o usuário será direcionado para outra etapa.
    if opcao == 1:
        pass
    elif opcao == 2:
        submenu_2(usuario)
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        exibir_informacoes_usuario(usuario)
    elif opcao == 6:
        pass

# Menu secundário
# Nesse código mostrará o segundo menu depois de no menu principal o usuário selecionar a opção
# 2. buscar rota -> Menu 2
# Mostrando a criação de uma nova rota, selecionar uma rota favorita ou já feita anteriormente 


# Esse script:
#Será responsável por qual rota o usuário deve prosseguir

# Tadeu Coêlho
# 13/08/2026

#------------------------
#info importante:
#Falta testar a integração com o resto das coisas
#===============================================================================================
# imports
#--------------------------------

#=====================================================
#Função para verficar e selecionar recorrentemente a opção do menu
#=====================================================

def submenu_2(usuario) -> int:

    # Simplifica o redirecionamento do usuário de acordo com a escolha
    def menu_interagir(opcao2):
        interator ={
            1:"criar_nova_rota()",
            2:"rotas_favoritas()",
            3:"rotas_favoritas()",
            4:menu(usuario)   # Falta integrar com usuário
        

        }
        interator[opcao2]

    print(
        f'\n[bold blue]{' BUSCAR ROTA ':=^40}[/]\n'
        '- Digite o número para realizar tal ação:\n'
        '1 - Criar nova rota\n'
        '2 - Selecionar dentre rotas Favoritas\n'
        '3 - Selecionar dentre rotas no Histórico\n' 
        '4 - Voltar\n'
        f'[bold blue]{'=' * 40}[/]'
    )       

    opcao2 = verificar_opcao(4)
    menu_interagir(opcao2)


    
