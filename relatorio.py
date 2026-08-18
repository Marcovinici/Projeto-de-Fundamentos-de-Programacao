from usuario import *
from rich import print

def contar_usuarios():
    cadastro = carregar_cadastro()
    return len(cadastro)


def contar_cadastros_hoje():
    cadastro = carregar_cadastro()
    quantidade = 0
    for usuario in cadastro:
        if cadastro[usuario]['data'] == date.today().strftime('%d/%m/%Y'):
            quantidade += 1
    return quantidade

def contar_rota_mais_pesquisada():
    pass



def exibir_relatorio():
    print(f'[bold blue]{' RELATÓRIO DO ADMINISTRADOR ':=^50}[/]')
    print(f'Quantidade de usuários cadastrados no sistema: {contar_usuarios()}')
    print(f'Quantidade de cadastros realizados hoje: {contar_cadastros_hoje()}')
    print(f'Rota mais pesquisada: {contar_rota_mais_pesquisada}')
    print(f'[bold blue]{'=' * 50}[/]')