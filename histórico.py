# Nesse código salvará o histórico de uso de um usuário
# Será necessário pois precisaremos para integrar na opção de ver rotas já feitas anteriormente 

# Tadeu Coêlho
# 14/08/2026

#------------------------
#info importante:
#Falta tetsar a integração com o resto das coisas
#Não testei se tem como aceitar usuário que não possui uma chave dentro de banco de dados chamada histórico
# ===============================================================================================
# imports
#--------------------------------


import json, os
from rich import print
from datetime import datetime

#=====================================================
#Função para verficar e selecionar recorrentemente a opção do menu
#=====================================================

ARQUIVO = "banco_de_dados.json"

# 1. Pega o caminho da pasta onde o arquivo 'salvar_historico.py' está localizado
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Une essa pasta com o nome do arquivo JSON
ARQUIVO = os.path.join(pasta_do_script, "banco_de_dados.json")
print(ARQUIVO)
def carregar_dados():
    with open(ARQUIVO, "r", encoding="utf-8") as file:
        return json.load(file)

    
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

def apagar_historico(nome): 
    dados = carregar_dados()

    if nome not in dados:
        print("Usuário não encontrado.")
        return

    dados[nome]["historico"] = {}
    print("Histórico Apagado")

    

def registrar_acao_usuario(nome, rota, paradas):
    dados = carregar_dados()

    if nome not in dados:
        print("Usuário não encontrado.")
        return

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nova_acao = {
        "rota": rota,
        "paradas": paradas,
        "data": agora
    }

    if "historico" not in dados[nome]:
        dados[nome]["historico"] = []

    dados[nome]["historico"].append(nova_acao)

    salvar_dados(dados)

    print(f"Ação registrada para {nome}.")

def mostrar_historico(nome):
    dados = carregar_dados()

    if nome not in dados:
        print("Usuário não encontrado.")
        return

    if "historico" not in dados[nome]:
        print("Usuário não possui histórico.")
        return

    if not dados[nome]["historico"]:
        dados[nome]["historico"] = {}
        return mostrar_historico(nome)
    
    if dados[nome]["historico"] == {}:
        print("Usuário não possui histórico.")
        return

    for viagem in dados[nome]["historico"]:
        print(f"\n[bold blue]{' HISTÓRICO ':=^40}[/]")
        print(f"Rota: {viagem['rota']}")
        print(f"Paradas: {' -> '.join(viagem['paradas'])}")
        print(f"Data: {viagem['data']}")
        print("-" * 30)
        
#Está retornando prints também, se quiserem podem tirar
#No teste que eu fiz, estava funcionando
