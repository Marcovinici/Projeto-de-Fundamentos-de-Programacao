import json


def exibir_mapa_ascii(dicionario_mapas, chave_quadrante=None):
    """
    Exibe a arte ASCII no terminal. 
    Se 'chave_quadrante' for fornecida, exibe apenas aquele mapa.
    Caso contrário, exibe todos os mapas armazenados no dicionário.
    """
    if not dicionario_mapas:
        print("-> Nenhum mapa disponível para exibição.")
        return

    # Exibe apenas um quadrante específico
    if chave_quadrante:
        chave_str = str(chave_quadrante)
        if chave_str in dicionario_mapas:
            print(f"\n=== MAPA DO QUADRANTE: {chave_str} ===")
            print(dicionario_mapas[chave_str])
        else:
            print(f"-> Quadrante {chave_str} não encontrado no dicionário.")
            
    # Exibe todos os mapas em sequência
    else:
        print(f"\nExibindo {len(dicionario_mapas)} mapas disponíveis:")
        for quadrante, arte in dicionario_mapas.items():
            print(f"\n=== MAPA DO QUADRANTE: {quadrante} ===")
            print(arte)
            
# Carrega os dados do arquivo gerado
try:
    with open("mapas_ascii.json", "r", encoding="utf-8") as f:
        meus_mapas = json.load(f)
        
    # Exemplo 1: Exibir apenas o primeiro quadrante mokado
    #exibir_mapa_ascii(meus_mapas, chave_quadrante="(0.0, 0.0)")
    
    # Exemplo 2: Para exibir TODOS os mapas de uma vez, basta omitir a chave:
    exibir_mapa_ascii(meus_mapas)
    
except FileNotFoundError:
    print("O arquivo 'mapas_ascii.json' ainda não foi criado.")
