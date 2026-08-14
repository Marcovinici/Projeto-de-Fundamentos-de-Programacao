# Versão atualizada da função "selecionar_rota()"

# Função para selecionar o ponto de origem

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

def selecionar_rota(pontos_candidatos):
    """
    Permite ao usuário selecionar um ponto de origem e um ponto de chegada
    de uma lista de pontos candidatos.

    Args:
        pontos_candidatos (list): Uma lista de strings representando os pontos disponíveis.

    Returns:
        list: Uma lista contendo o ponto de origem e o ponto de chegada escolhidos.
    """
    pontos_disponiveis = list(pontos_candidatos) # Cria uma cópia para não modificar a lista original, para facilitar funcionamento o ideal seria designar números aos possíveis pontos, semelhante ao menu principal
    pontos_escolhidos = []

    ponto_partida, chegadas_uteis = selecionar_origem(pontos_candidatos)

# Se o usuário escolheu '0' na origem, encerra a função retornando lista vazia
    if ponto_partida is None:
        print("Retornando ao menu...")
        return []
    
    ponto_destino = selecionar_chegada(chegadas_uteis)
    
    if ponto_partida is not None and ponto_destino is None:
        print("Retornando ao menu...")
        return []
   

    pontos_escolhidos.append(ponto_partida[0])
    pontos_escolhidos.append(ponto_destino[0])

    return pontos_escolhidos

# Testes
pontos_teste = ["1", "2", "3"]
rota = selecionar_rota(pontos_teste)

if not rota:
    print("Ação cancelada pelo usuário.")
else:
    print(f"Rota selecionada: {rota}")