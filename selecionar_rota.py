# Versão inicial da função "selecionar_rota()" (Caminho: 2. Buscar rota ---> 1. Criar nova rota)

def selecionar_rota(pontos_candidatos):
    """
    Permite ao usuário selecionar um ponto de origem e um ponto de chegada
    de uma lista de pontos candidatos.

    Args:
        pontos_candidatos (list): Uma lista de strings representando os pontos disponíveis.

    Returns:
        list: Uma lista contendo o ponto de origem e o ponto de chegada escolhidos.
    """
    pontos_disponiveis = list(pontos_candidatos) # Cria uma cópia para não modificar a lista original
    pontos_escolhidos = []

    # Loop para selecionar o ponto de origem
    while True:
        print(f"Opções disponíveis: {', '.join(pontos_disponiveis)}")
        origem = input("Insira o ponto de origem: ")
        if origem in pontos_disponiveis:
            pontos_escolhidos.append(origem) # Adiciona o ponto à rota
            pontos_disponiveis.remove(origem) # Retira o ponto dos pontos disponíveis
            break
        else:
            print("Escolha uma opção disponível.")

    # Loop para selecionar o ponto de chegada
    while True:
        print(f"Opções disponíveis: {', '.join(pontos_disponiveis)}")
        chegada = input("Insira o ponto de chegada: ")
        if chegada in pontos_disponiveis:
            pontos_escolhidos.append(chegada) # Adiciona o ponto à rota
            pontos_disponiveis.remove(chegada) # Retira o ponto dos pontos disponíveis
            break
        else:
            print("Escolha uma opção disponível.")

    return pontos_escolhidos

# Exemplo de uso da função:
meus_pontos = ["Parque Central", "Shopping Cidade", "Estação Metrô", "Biblioteca Pública"]

print("\n--- Seleção da Rota ---")
rota_selecionada = selecionar_rota(meus_pontos)

print(f"\nVocê selecionou a rota: {rota_selecionada[0]} -> {rota_selecionada[1]}")
