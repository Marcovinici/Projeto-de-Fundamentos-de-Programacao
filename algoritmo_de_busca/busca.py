# Importando deque
from collections import deque 

# Função para printar matriz
def printMatriz(matriz, rota):
    for i, linha in enumerate(matriz):
        for j, coluna in enumerate(linha):
            # Se (i,j) pertencer a caminho, no lugar do espaço em branco é printado o +
            if (i, j) in rota:
                print("+", end="")
            else:
                print(coluna, end="")
        print()
        
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
        matriz[linha][coluna] != '#' and \
        not visitado[linha][coluna]

# Algoritmo para achar o caminho mais curto
def caminhoBFS(matriz):

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

            if matriz[i][j] == 'A':

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
        if matriz[linha][coluna] == 'B':

            # Cria a rota utilizando a lista de pais e printa a matriz
            # OBS: Acho melhor o código ser alterado para retornar a matriz, em vez de só printar
            rota = cria_rota(inicio, (linha, coluna), pais)
            printMatriz(matriz, rota)

            return distancia

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

# Execução com uma matriz exemplo

# Abre arquivo .txt e transforma em matriz 
arquivo = open("caminho.txt", "r")
caminho = arquivo.read()
print("Esse é um caminho exemplo")
print(caminho)

print("_"*40,"\n")
arquivo.seek(0)

matriz = []
for linha in arquivo:
    matriz.append(list(linha.rstrip("\n")))

print(caminhoBFS(matriz))