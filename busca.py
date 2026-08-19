# Importando deque
from collections import deque 
# Bibliotecas para manipular os arquivos
from pathlib import Path
import json
# Importações do Rich para a impressão colorida
from rich.console import Console
from rich.text import Text


# Função responsável por converter o arquivo json em uma matriz
def formata_mapa(arquivo):

    mapa = arquivo["(0.0, 0.0)"]

    # Criando matriz
    matriz = []
    for linha in mapa.splitlines():
        matriz.append(list(linha))

    # Eliminando elemetos
    
    for linha in matriz:
        for i, caractere in enumerate(linha):
            # Verificando se caractere não é um #, ou qualquer caractere que representa uma localidade
            if caractere not in ["F" ,"R", "H", "S", "P", "p", "E", "I", "#"]:
                linha[i] = " "

    return matriz

# Abaixo temos funções usadas em caminhoBFS()

# Função para criar arquivo com nova rota
def novaMatriz(matriz, rota, destino):

    with open("novo_mapa.txt", "w") as novo_mapa:
        for i, linha in enumerate(matriz):
            for j, coluna in enumerate(linha):
                # Se (i,j) pertencer a caminho, no lugar do espaço em branco é printado o +
                if (i, j) in rota:
                    if coluna != destino:
                        novo_mapa.write("+")
                    else:
                        novo_mapa.write(coluna)
                else:
                    novo_mapa.write(coluna)

            novo_mapa.write("\n")
    return novo_mapa
     
# Função para construir a rota
def cria_rota(inicio, destino_encontrado, pais):
    rota = []
    while destino_encontrado != inicio:
        rota.append(destino_encontrado)
        destino_encontrado = pais[destino_encontrado]
    return rota

# Função validadora de coordenada(caminho):
# Checa se posição na matriz faz parte da estrada e se já não foi visitada
def validacao(linha, coluna, n, m, matriz, visitado):
    
    return linha >= 0 and linha < n and \
        coluna >= 0 and coluna < m and \
        matriz[linha][coluna] != ' ' and \
        not visitado[linha][coluna]


# Algoritmo para achar o caminho mais curto
def caminhoBFS(matriz, partida, destino):

    total_linhas = len(matriz)    
    total_colunas = len(matriz[0])

    # Direções de movimento: esquerda, direita, para baixo e para cima
    dlinha = [-1, 1, 0, 0]
    dcoluna = [0, 0, -1, 1]

    # Dicionário para guardar o pai de cada posição
    pais = {} 

    # matriz de visitados, inicia com todas as posições disponíveis(nesse caso, com valor False)
    visitado = [[False for _ in range(total_colunas)] for _ in range(total_linhas)]

    # Fila do BFS: armazena a linha, a coluna, e a distância do ponto de origem
    fila = deque()
    # Procurando o ponto de partida
    # e iniciando o BFS dele
    for i in range(total_linhas):
        for j in range(total_colunas):

            if matriz[i][j] == partida:

                fila.append([i, j, 0])

                visitado[i][j] = True

                inicio = (i, j)

                break

    # Loop BFS
    while fila:

        atual = fila.popleft()

        linha = atual[0]
        coluna = atual[1]
        distancia = atual[2]

        # Se o destino for encontrado, retorna a matriz e a distância do menor caminho
        if matriz[linha][coluna] == destino:

            # Cria a rota utilizando a lista de pais e printa a matriz
            # OBS: Acho melhor o código ser alterado para retornar a matriz, em vez de só printar
            rota = cria_rota(inicio, (linha, coluna), pais)
            novaMatriz(matriz, rota, destino)

        # Caso o destino não for encontrado, vamos verificar as 4 posições adjacentes as coordenadas atuais
        for i in range(4):

            nova_linha = linha + dlinha[i]
            nova_coluna = coluna + dcoluna[i]

            # Se a coordenada for válida e não tiver sido visitada:
            if validacao(nova_linha, nova_coluna, total_linhas, total_colunas, matriz, visitado):

                # Marca a coordenada como visitada
                visitado[nova_linha][nova_coluna] = True

                # Guardando pai da nova posição
                pais[nova_linha, nova_coluna] = (linha, coluna)

                # É adicionada a fila com sua respectiva distância
                fila.append([nova_linha, nova_coluna, distancia + 1])

    # Se nenhum caminho for encontrado retorna "Erro"
    return "Erro"

# Função do mapa_principal
def mapa_principal():
    '''
    Cria o mapa_principal a partir do arquivo mapas_ascii.json
    '''
    arquivo = Path(__file__).parent / "mapas_ascii.json"
    arquivo = open(arquivo, "r")
    arquivo = json.load(arquivo)

    with open("mapa_principal", "w") as mapa_principal:
        mapa_principal.write(arquivo["(0.0, 0.0)"])


# Função responsável por imprimir o arquivo do mapa com cores no terminal
def imprimir_mapa_colorido_text(caminho_arquivo):
    console = Console()
    
    # Mapeamento de caracteres para estilos de cor do Rich
    estilos = {
		" ": "navy_blue",
        "+": "dark_red",     # Caminho percorrido em ciano negrito
        "#": "bright_black",  # Estradas/Paredes em cinza escuro
        "R": "bold yellow",   # Localidades em amarelo negrito
        "H": "bold yellow",
        "S": "bold yellow",
        "P": "bold yellow",  
        "p": "bold yellow",  
        "E": "bold yellow",
        "I": "bold yellow",  
        "F": "bold yellow",
    }
    
    texto_formatado = Text()
    
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            for char in linha:
                # Pega a cor correspondente ou usa a cor padrão da fonte
                estilo = estilos.get(char, "default")
                texto_formatado.append(char, style=estilo)
                
    console.print(texto_formatado)
    
    
# Abaixo temos a função principal

def buscar(pontos):
    '''
    A função recebe como argumentos os pontos de partida e de chegada e imprimi o mapa com caminho mais curto
    '''
    try:# Preparando arquivo json
        arquivo = Path(__file__).parent / "mapas_ascii.json"
        arquivo = open(arquivo, "r")
        arquivo = json.load(arquivo)
    
    except FileNotFoundError:
        print("O arquivo 'mapas_ascii.json' ainda não foi criado.")
        return None

    # Definindo o ponto de partida e o de chegada
    partida = pontos[0]
    destino = pontos[1]

    mapa = formata_mapa(arquivo)
    caminhoBFS(mapa, partida, destino)

    # Printando mapa colorido
    #imprimir_mapa_colorido_text("novo_mapa.txt")
