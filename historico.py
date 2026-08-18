#Esse Código lidará com o histórico do usuário
# Tadeu Coêlho

#---------------------------------------------------------------------------------

#Como usar
#registrar_historico(usuario, rota)             registra no banco de dados uma ação do usuário
#apagar_historico(usuario)                      apaga TOdo o histórico do usuario
#mostrar_historico                              printa uma tabela do histórico do usuário



# ===============================================================================================
# imports
#--------------------------------
import json, os
from rich import print
from datetime import datetime

#=====================================================
#Funções para facilitar a pegar o arquivo json
#=====================================================

ARQUIVO = "banco_de_dados.json"

# 1. Pega o caminho da pasta onde o arquivo 'historico.py' está localizado
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Une essa pasta com o usuario do arquivo JSON
ARQUIVO = os.path.join(pasta_do_script, "banco_de_dados.json")

#=====================================================
#Funções para pegar os dados no banco de dados e a outra salva no banco de dados 
#=====================================================

def carregar_dados():
    with open(ARQUIVO, "r", encoding="utf-8") as file:
        return json.load(file)

    
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

#=====================================================
#Função para apagar o histórico de um usuário
#=====================================================

def apagar_historico(usuario): 
    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return

    dados[usuario]["historico"] = []
    salvar_dados(dados)
    print(f"Histórico do usuário: {usuario}, apagados")

    
#=====================================================
#Função para registrar o histórico de um usuário
#=====================================================

def registrar_historico(usuario, rota):
    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return

    agora = datetime.now().strftime("%Y-%m-%d %H:%M")

    nova_acao = {
        "rota": rota,
        "data": agora
    }

    if "historico" not in dados[usuario]:
        dados[usuario]["historico"] = []

    dados[usuario]["historico"].append(nova_acao)

    salvar_dados(dados)

#=====================================================
#Função para mostrar o histórico de um usuário
#=====================================================

def mostrar_historico(usuario):
    dados = carregar_dados()

    if usuario not in dados:
        print("Usuário não encontrado.")
        return

    if "historico" not in dados[usuario]:
        dados[usuario]["historico"] = []
        salvar_dados(dados)
        print("Usuário não possui histórico.")
        return

    if not dados[usuario]["historico"]:
        print("Usuário não possui histórico.")
        return 
    
    if dados[usuario]["historico"] == []:
        print("Usuário não possui histórico.")
        return


    print(f"\n[bold blue]{' HISTÓRICO ':=^40}[/]")
    for viagem in dados[usuario]["historico"]:
        print(f"Rota: {viagem['rota']}")
        print(f"Data: {viagem['data']}")
        print("-" * 30)
