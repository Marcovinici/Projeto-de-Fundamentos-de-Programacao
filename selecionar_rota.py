# Versão atualizada da função "selecionar_rota()"

# Função para selecionar o ponto de origem
import json
import os

arquivo_rotas = "rotas.json"
# Função para carregar rotas salvas do arquivo JSON
def carregar_rotas():
    if not os.path.exists(arquivo_rotas):
        return {}
    try:
        with open(arquivo_rotas, "r", encoding="utf-8") as arquivo:
            rotas =  json.load(arquivo)

            if not isinstance(rotas, dict):
                return {}
            
            return rotas
    except (json.JSONDecodeError, FileNotFoundError):
        return {}
# Função para salvar uma rota no arquivo JSON
def salvar_rota(nome_rota, rota):
    rotas = carregar_rotas()
    rotas[nome_rota] = rota

    with open(arquivo_rotas, "w", encoding="utf-8") as arquivo:
        json.dump(rotas, arquivo, ensure_ascii=False, indent=4)
    print(f"Rota '{nome_rota}' salva com sucesso.")

# Função para selecionar uma rota salva
def selecionar_rota_salva():
    rotas = carregar_rotas()
    if not rotas:
        print("Nenhuma rota salva encontrada.")
        return None

    nomes_rotas = list(rotas.keys())
    print("\nRotas salvas:")
    for i, nome in enumerate(nomes_rotas, start=1):
        print(f"{i} -> {nome}: {rotas[nome]}")
        
    while True:
        escolha = input("Escolha uma rota (ou digite '0' para voltar): ")
        if escolha == '0':
            return None
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(nomes_rotas):
              nome_escolhido = nomes_rotas[indice]
              return rotas[nome_escolhido]
        print("Escolha uma opção disponível.")

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
   

    pontos_escolhidos = [
    ponto_partida[0], 
    ponto_destino[0]
    ]

    print(f"Rota selecionada: {pontos_escolhidos}")

    salvar = input("Deseja salvar esta rota? (s/n): ").lower()

    if salvar == 's':
        nome_rota = input("Digite um nome para a rota: ")
        salvar_rota(nome_rota, pontos_escolhidos)


        return pontos_escolhidos

# Testes
pontos_teste = ["1", "2", "3"]
rota = selecionar_rota(pontos_teste)

if not rota:
    print("Ação cancelada pelo usuário.")
else:
    print(f"Rota selecionada: {rota}")

    print("\n--- TESTE DE CARREGAMENTO ---")

    rota = selecionar_rota_salva()

    if rota is None:
        print("Nenhuma rota foi carregada.")
    else:
        print(f"Rota carregada com sucesso: {rota}")

"""
def menu_favoritos(usuario, rota):
    print("")
    interator ={
        1:registrar_favoritos(usuario, rota),
        2:"Voltar para a seleção de rotas()", # Depende do povo que fizer a seleção de rotas, se quiserem tirar isso ou somente deixar para ir ao menu principal de novo ou add aos fav
        3:menu(usuario)  
    

    }
    interator[opcao2]

    print(
        f'\n[bold blue]{' Deseja adicionar os favoritos? ':=^40}[/]\n'
        '- Digite o número para realizar tal ação:\n'
        '1 - Adcionar rota aos favoritos! \n'
        '2 - Não adiconar rota e Voltar \n' #ao menu de seleção de rotas
        '3 - Ir ao menu principal\n' 
        f'[bold blue]{'=' * 40}[/]'
    )       

    opcao2 = verificar_opcao(3)
    menu_favoritos(opcao2)
    """
