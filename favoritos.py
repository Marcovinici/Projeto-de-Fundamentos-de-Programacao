# Esse Código lidará com os FAVORITOS do usuário
# Tadeu Coêlho

#---------------------------------------------------------------------------------

#Como usar
#registrar_favoritos(usuario, rota)              Registra no banco de dados uma rota favorita do usuário
#apagar_favoritos(usuario)                       Apaga TOdos os favoritos do usuario
#mostrar_favoritos(usuario)                      Printa uma tabela dos favoritoss do usuário
#menu_favoritos(usuario, rota) #Não funcionando  Pergunta ao usuário se gostaria de salvar a rota, volta ao menu principal ou algo que queiram em 2(sla um menu de selecionar a rota)


#Menu dos favoritos não está funcionando
#Falta comentar intrafunção

# ===============================================================================================
# imports
#--------------------------------

import json, os
from rich import print
from datetime import datetime
from historico import carregar_dados, salvar_dados


#=====================================================
#Funções para facilitar a pegar o arquivo json
#=====================================================


ARQUIVO = "banco_de_dados.json"

# 1. Pega o caminho da pasta onde o arquivo 'salvar_favoritos.py' está localizado
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Une essa pasta com o usuario do arquivo JSON
ARQUIVO = os.path.join(pasta_do_script, "banco_de_dados.json")

#=====================================================
#Função para apagar os favoritos de um usuário
#=====================================================

def apagar_favoritos(usuario): 
    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return

    dados[usuario]["favoritos"] = []
    salvar_dados(dados)
    print(f"Dados dos favoritos do usuário {usuario}, apagados")

    
    
#=====================================================
#Função para registrar os favoritos de um usuário
#=====================================================


def registrar_favoritos(usuario, rota):
    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return

    agora = datetime.now().strftime("%Y-%m-%d %H:%M")

    rota_fav = {
        "rota": rota,
        "data": agora
    }

    if "favoritos" not in dados[usuario]:
        dados[usuario]["favoritos"] = []

    dados[usuario]["favoritos"].append(rota_fav)

    salvar_dados(dados)

    print(f"Rota favorita salva do usuário: {usuario}.")



#=====================================================
#Função para mostrar os favoritos de um usuário
#=====================================================

def mostrar_favoritos(usuario):
    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return

    if "favoritos" not in dados[usuario]:
        dados[usuario]["favoritos"] = []
        salvar_dados(dados)
        print("Usuário não possui favoritos.")
        return

    if not dados[usuario]["favoritos"]:
        print("Usuário não possui favoritos.")
        return 
    
    if dados[usuario]["favoritos"] == []:
        print("Usuário não possui favoritos.")
        return


    print(f"\n[bold blue]{' FAVORITOS ':=^40}[/]")
    for viagem in dados[usuario]["favoritos"]:
        print(f"Rota: {viagem['rota']}")
        print(f"Data: {viagem['data']}")
        print("-" * 30)
        
#=====================================================
#Função menu dos favoritos, perguntando se o usuário, que acabou de usar uma rota, se ele gostaria de salvála nos favoritos
#não funcionando
#=====================================================


