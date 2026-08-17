# Nesse código salvará o histórico de uso de um usuário
# Será necessário pois precisaremos para integrar na opção de ver rotas já feitas anteriormente 

# Tadeu Coêlho
# 14/08/2026

#------------------------
#info importante:
#Falta tetsar a integração com o resto das coisas
# ===============================================================================================
# imports
#--------------------------------


import json
import os
from datetime import datetime

#=====================================================
#Função para verficar e selecionar recorrentemente a opção do menu
#=====================================================

ARQUIVO = "banco_de_dados.json"

# 1. Pega o caminho da pasta onde o arquivo 'salvar_historico.py' está localizado
pasta_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Une essa pasta com o nome do arquivo JSON
ARQUIVO = os.path.join(pasta_do_script, "banco_de_dados.json")

def carregar_dados():
    with open(ARQUIVO, "r", encoding="utf-8") as file:
        return json.load(file)

    
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

def inicializar_ou_apagador_banco():         #AVISO: APAGADOR DE BANCO DE DADOS!! Usem somente se necessário 
    if not os.path.exists(ARQUIVO):
        salvar_dados({"usuario": []})

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

#Está retornando prints também, se quiserem podem tirar
#No teste que eu fiz, estava funcionando
