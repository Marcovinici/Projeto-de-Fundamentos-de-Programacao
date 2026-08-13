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
    print("2. Buscar rota")
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