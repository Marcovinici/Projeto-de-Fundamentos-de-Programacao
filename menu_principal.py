# Exemplo de menu principal
# É uma gama de opções que aparece após o usuário efetuar o login ou se cadastrar no sistema

from rich import print

# Verifica se uma opção é inteira e está no intervalo correto.
def verificar_opcao() -> int:
    try:
        opcao = int(input("Escolha uma opção: "))
        while not 1 <= opcao <= 6:  # Abre um loop caso a opção esteja no intervalo incorreto
            print("Digite uma opção no intervalo especificado. Tente novamente!")
            opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("[red]Certifique-se de digitar um número inteiro. Tente novamente![/]")
        verificar_opcao()  # Reinicia a verificação se o tipo for incorreto


def menu(usuario):

    print(f"[bold blue]{' MENU ':=^40}[/]")
    print(f"O que deseja fazer {usuario}?")
    print("1. Visualizar mapa")
    print("2. Buscar rota")                         #
    print("3. Ver histórico de rotas pesquisadas")
    print("4. Ver rotas favoritas")
    print("5. Informações sobre o usuário")
    print("6. Sair da sessão")
    print(f"[bold blue]{'=' * 40}[/]")

    opcao = verificar_opcao()
    
    # Dependendo da entrada, o usuário será direcionado para outra etapa.
    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        pass
    elif opcao == 6:
        pass

menu("Jorge")


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
#Falta tetsar a integração com o resto das coisas
#===============================================================================================
# imports
#--------------------------------

#=====================================================
#Função para verficar e selecionar recorrentemente a opção do menu
#=====================================================

def menu_2(usuario) -> int:

    def opcoes_do_menu2():
                      
        try:    #Sempre printar as opções do menu junto com a parte de escolher as opções
            print(
                f'\n[bold blue]{' MENU ':=^40}[/]") - Digite o número para realizar tal ação:\n'
                '1 - Criar nova rota\n'
                '2 - Selecionar dentre rotas Favoritas\n'
                '3 - Selecionar dentre rotas no Histórico\n' 
                '4 - Voltar\n'
                '\n'
        ) 
            opcao2 = int(input("Escolha uma opção: "))
            while not 1 <= opcao2 <= 4:  # Abre um loop caso a opção esteja no intervalo incorreto
                print("Digite uma opção no intervalo especificado. Tente novamente!")
                opcao2 = int(input("Escolha uma opção: "))
                
            return opcao2
        except ValueError:
            print("[red]Certifique-se de digitar um número inteiro. Tente novamente![/]")
            opcoes_do_menu2()  # Reinicia a verificação se o tipo for incorreto            

            #falta integrar com outros sistemas   
    def menu_interagir(opcao2):
        interator ={
            1:"criar_nova_rota()",
            2:"rotas_favoritas()",
            3:"rotas_favoritas()",
            4:menu(usuario)   #falta integrar com usuário
        

        }
        interator[opcao2]
