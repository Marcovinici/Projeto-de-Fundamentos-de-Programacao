# Versão atualizada da função "selecionar_rota()"
#código integrado com os favoritos

# Função para selecionar o ponto de origem
import json
import os
from favoritos import registrar_favoritos

arquivo_rotas = "rotas.json"
banco_de_dados = "banco_de_dados.json"

#função para selecionar o ponto de origem
def selecionar_origem(pontos_candidatos):
  chegadas_disponiveis = list(pontos_candidatos)
  origens_disponiveis = list(pontos_candidatos)
  origem_selecionada = []

  while True:
    print(f"Opções disponíveis: {', '.join(origens_disponiveis)}")
    origem = input("Insira o ponto de origem (ou digite '0' para voltar): ")
    if origem == '0':
            return None, None # Sinaliza cancelamento/retorno

    if origem in origens_disponiveis:
      origem_selecionada.append(origem) # Adiciona o ponto à rota
      chegadas_disponiveis.remove(origem)
      break
    else:
      print("Escolha uma opção disponível.")

  return origem_selecionada, chegadas_disponiveis



# Função para selecionar o ponto de chegada
def selecionar_chegada(pontos_candidatos):
  chegadas_disponiveis = list(pontos_candidatos)
  chegada_escolhida = []

  while True:
    print(f"Opções disponíveis: {', '.join(chegadas_disponiveis)}")
    chegada = input("Insira o ponto de chegada (ou digite '0' para voltar): ")

    if chegada == '0':
            return None # Sinaliza cancelamento/retorno

    if chegada in chegadas_disponiveis:
        chegada_escolhida.append(chegada) # Adiciona o ponto à rota
        break
    else:
        print("Escolha uma opção disponível.")

  return chegada_escolhida

# Função designada para criar uma nova rota ao receber origem e destino. (Caminho: 2. Buscar rota --> 1. Criar nova rota)

def selecionar_rota(pontos_candidatos, usuario_logado=None):
    
    """
    Permite ao usuário selecionar um ponto de origem e chegada.
    Se um usuario_logado for passado, pergunta se ele quer salvar nos favoritos
    usando a função 'registrar_favoritos' do arquivo 'favoritos.py'.
    """
    pontos_disponiveis = list(pontos_candidatos) 
    
    ponto_partida, chegadas_uteis = selecionar_origem(pontos_candidatos)

    if ponto_partida is None:
        print("Retornando ao menu...")
        return []
    
    ponto_destino = selecionar_chegada(chegadas_uteis)
    
    if ponto_destino is None:
        print("Retornando ao menu...")
        return []

    # Monta a rota final
    pontos_escolhidos = [ponto_partida[0], ponto_destino[0]]
    print(f"\nRota selecionada: {pontos_escolhidos}")

    if usuario_logado:
        salvar = input("Deseja salvar esta rota nos favoritos? (s/n): ").strip().lower()

    if salvar == 's':
        registrar_favoritos(usuario_logado, pontos_escolhidos)
        print("Rota salva nos favoritos.")
    else:
        print("Nenhum usuário logado. Rota não salva nos favoritos.")

    return pontos_escolhidos

# --- TESTE DO CÓDIGO ---
'''
if __name__ == "__main__":
    pontos_teste = ["1", "2", "3"]
    # Simulando que o usuário 'Pedro' está logado no sistema
    usuario_atual = "Pedro" 
    
    rota = selecionar_rota(pontos_teste, usuario_atual)
'''