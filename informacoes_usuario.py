# Esse script:
# Seção de exibição de informações do usuário, como data de criação da conta, histórico de rotas, rotas favoritas e outras informações pertinentes.

# Alysson - 14.08.26

from rich import print
from usuario import carregar_cadastro
import json

def exibir_informacoes_usuario(usuario):
    cadastro = carregar_cadastro()

    if usuario in cadastro:
        info_usuario = cadastro[usuario]

        print(f"\n[bold blue]{' INFORMAÇÕES DO USUÁRIO ':=^40}[/]")

        print(f"Usuário: [yellow]{usuario}[/]")

        data = info_usuario.get("data", "Não disponível")
        historico = info_usuario.get("historico_rotas", "Não disponível")
        favoritos = info_usuario.get("rotas_favoritas", "Não disponível")

        print(f"Data de criação da conta: {data if data != 'Não disponível' else '[yellow]Não disponível[/]'}")
        print(f"Histórico de rotas: {historico if historico != 'Não disponível' else '[yellow]Não disponível[/]'}")
        print(f"Rotas favoritas: {favoritos if favoritos != 'Não disponível' else '[yellow]Não disponível[/]'}")

        return cadastro, info_usuario 

        # Esperando o desenvolvimento de funcionalidades futuras,
        # como histórico de rotas e rotas favoritas.

    else:
        print("Usuário não encontrado.")


def redefinir_senha(cadastro, info_usuario):
    senha_antiga = input("Senha antiga: ")
    senha_nova = input("Senha nova: ")

    if senha_nova == senha_antiga:
        print("A nova senha não pode ser igual à antiga.")
        return redefinir_senha(cadastro, info_usuario)

    elif senha_antiga == info_usuario.get('senha'):
        info_usuario['senha'] = senha_nova

        with open('banco_de_dados.json', 'w') as arquivo:
            json.dump(cadastro, arquivo, indent=4)

        print("Senha alterada com sucesso!")

    else:
        print("Senha antiga incorreta.")