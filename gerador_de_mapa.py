import osmnx as ox
from PIL import Image, ImageDraw
import os
import math
import time
import json

# ==========================================
# PARTE 1: ENTRADA E TRATAMENTO DE COORDENADAS
# ==========================================

def separar_dms(coordenada_str):
    """
    Recebe uma string como '7°12'54" S' e separa em graus, minutos, segundos e direção.
    """
    texto_limpo = coordenada_str.replace("°", " ").replace("'", " ").replace('"', " ")
    partes = texto_limpo.split()
    
    if len(partes) == 4:
        return (float(partes[0]), float(partes[1]), float(partes[2]), partes[3].upper())
    else:
        raise ValueError(f"Formato não reconhecido: {coordenada_str}")

def converter_para_decimal(graus, minutos, segundos, direcao):
    """
    Converte os valores separados para grau decimal.
    """
    decimal = graus + (minutos / 60) + (segundos / 3600)
    if direcao.upper() in ['S', 'O', 'W']:
        decimal *= -1
    return decimal

def ler_coordenadas(nome_do_ponto="Ponto", mokado_lat=None, mokado_lon=None):
    """
    Lê a latitude e longitude e retorna a tupla (lat_decimal, lon_decimal).
    Implementa um loop caso as coordenadas sejam mal definidas.
    """
    print(f"\n--- Lendo {nome_do_ponto} ---")
    print("Formato aceito: 7°12'54\" S ou 7 12 54 S")
    
    while True:
        if (mokado_lat is None) and (mokado_lon is None):
            str_lat = input("Latitude: ")
            str_lon = input("Longitude: ")
        else:
            str_lat = mokado_lat
            str_lon = mokado_lon
        
        try:
            partes_lat = separar_dms(str_lat)
            partes_lon = separar_dms(str_lon)
            
            latitude_decimal = converter_para_decimal(*partes_lat)
            longitude_decimal = converter_para_decimal(*partes_lon)

            return (latitude_decimal, longitude_decimal)
            
        except Exception:
            print("As coordenadas foram mal definidas. Tente novamente.")
            time.sleep(3) # Pausa por 3 segundos antes de recomeçar o loop


# ==========================================
# PARTE 2: GEOMETRIA E GRADES (BOUNDING BOX)
# ==========================================

def determinar_bbox_geral(ponto1, ponto2):
    """
    Entrada: Duas tuplas (lat, lon) em graus decimais.
    Saída: Tupla (norte, sul, leste, oeste).
    """
    try:
        p1_latitude, p1_longitude = ponto1
        p2_latitude, p2_longitude = ponto2

        norte = max(p1_latitude, p2_latitude)
        sul = min(p1_latitude, p2_latitude)
        leste = max(p1_longitude, p2_longitude)
        oeste = min(p1_longitude, p2_longitude)
        
        return (norte, sul, leste, oeste)
    except Exception as e:
        print(f"Erro ao determinar BBox: {e}")
        return None

def dividir_bbox_em_grade(bbox_geral, largura_caracteres=80, altura_caracteres=40, tamanho_lado_metros=4.0):
    """
    Entrada: Tupla (N, S, L, O) e definições da grade.
    Saída: Dicionário contendo sub-BBoxes perfeitamente dimensionadas para 80x40 caracteres.
    """
    if not bbox_geral:
        return None
        
    norte, sul, leste, oeste = bbox_geral
    
    # 1. Calcula o tamanho físico total de cada sub-bbox em metros
    largura_m = largura_caracteres * tamanho_lado_metros # 80 * 4 = 320m
    altura_m = altura_caracteres * tamanho_lado_metros   # 40 * 4 = 160m
    
    # 2. Correção por latitude (fator de distorção longitudinal)
    lat_media = (norte + sul) / 2.0
    lat_rad = math.radians(lat_media)
    
    # 3. Conversão da medida física (metros) para graus decimais
    metros_por_grau_lat = 111132.0
    metros_por_grau_lon = 111320.0 * math.cos(lat_rad)
    
    passo_lat = altura_m / metros_por_grau_lat
    passo_lon = largura_m / metros_por_grau_lon

    dicionario_bboxes = {}

    # 4. Varredura gerando as BBoxes
    lat_atual = norte
    while lat_atual > sul:
        sul_sub = lat_atual - passo_lat 
        
        lon_atual = oeste
        while lon_atual < leste:
            leste_sub = lon_atual + passo_lon 
            
            chave_noroeste = (lat_atual, lon_atual)
            # Salvo direto como tupla para o desempacotamento na função de desenhar funcionar
            dicionario_bboxes[chave_noroeste] = (lat_atual, sul_sub, leste_sub, lon_atual)
            
            lon_atual += passo_lon
            
        lat_atual -= passo_lat
        
    return dicionario_bboxes


# ==========================================
# PARTE 3: CONVERSÃO DE IMAGEM PARA ASCII
# ==========================================


def conversor_ASCII(imagem):
    """
    Recebe um objeto PIL.Image gerado em memória e mapeia os 
    pixels exatos para caracteres.
    Converte imagens para binárias, usando apenas espaços e um caractere único.
    """
    # Caractere único para áreas "brancas" (o conteúdo do mapa)
    caractere_branco = "#"
    
    # Limiar (threshold) para separar o que é "preto" do que é "branco"
    # Valores de 0-255. Valores abaixo disto viram espaço (" "), acima viram o caractere (#).
    # 128 é o valor central. Ajuste este valor se o seu mapa for muito escuro ou muito claro.
    threshold = 128
    
    try:
        # Garante que a imagem esteja no modo 'L' (Tons de Cinza/Luminosidade)
        # Se for RGB ou RGBA, converterá para tons de cinza matematicamente.
        # Isto é necessário para obtermos valores únicos de luminosidade por pixel.
        if imagem.mode != 'L':
            img_processada = imagem.convert('L')
        else:
            img_processada = imagem
            
        # Pega a matriz de luminosidade 
        pixels = list(img_processada.getdata())
        ascii_arte = ""
        largura_atual = img_processada.size[0]
        
        for i, brilho in enumerate(pixels):
            # Áreas escuras abaixo do limiar viram espaço vazio (" ")
            if brilho < threshold:
                ascii_arte += " "
            # Áreas claras acima do limiar viram o caractere único (#)
            else:
                ascii_arte += caractere_branco
            
                
        return ascii_arte
    except Exception as e:
        print(f"Erro ao converter imagem para ASCII binário: {e}")
        return None

# ==========================================
# PARTE 4: PIPELINE DO MAPA PARA CARACTERES E ARMAZENAMENTO
# ==========================================

def gerar_ascii_por_recorte(caminho_img, bbox_total, sub_bbox, largura_caracteres=80, altura_caracteres=40):
    """
    Calcula a proporção da sub_bbox em relação à bbox_total e 
    recorta a parte correspondente da imagem local para gerar o ASCII.
    """
    try:
        if not os.path.exists(caminho_img):
            print(f" -> Erro: O arquivo '{caminho_img}' não foi encontrado.")
            return None
            
        # 1. Abre a imagem e converte para tons de cinza
        img = Image.open(caminho_img).convert("L")
        
        # 2. A MÁGICA ACONTECE AQUI: Filtro de alto contraste!
        # Como as ruas são brancas (luminosidade > 127) e o resto é cinza/escuro,
        # forçamos a rua a ficar 255 (branco) e o resto a sumir virando 0 (preto).
        # Ajuste esse "240" para mais ou menos se as ruas estiverem grossas/finas demais.
        img = img.point(lambda p: 255 if p > 127 else 0)
        
        largura_img, altura_img = img.size
        
        N, S, L, O = bbox_total
        n_sub, s_sub, l_sub, o_sub = sub_bbox
        
        # Evita divisão por zero
        if L == O or N == S:
            return None
            
        # Calcula as coordenadas do recorte em pixels com base na latitude/longitude
        x_min = int(((o_sub - O) / (L - O)) * largura_img)
        x_max = int(((l_sub - O) / (L - O)) * largura_img)
        y_min = int(((N - n_sub) / (N - S)) * altura_img) # Norte é o topo da imagem (Y=0)
        y_max = int(((N - s_sub) / (N - S)) * altura_img)
        
        # Tratamento de segurança para não extrapolar os limites da imagem
        x_min, x_max = max(0, min(x_min, x_max)), min(largura_img, max(x_min, x_max))
        y_min, y_max = max(0, min(y_min, y_max)), min(altura_img, max(y_min, y_max))
        
        if x_min == x_max or y_min == y_max:
            return None
            
        recorte = img.crop((x_min, y_min, x_max, y_max))
        recorte_redimensionado = recorte.resize((largura_caracteres, altura_caracteres))
        
        arte = conversor_ASCII(recorte_redimensionado)
        img.close()
        
        return arte
        
    except Exception as e:
        print(f" -> Erro ao processar recorte da imagem: {e}")
        return None
        
        
#Não funcionou por algum erro no servidor
def gerar_ascii_do_mapa(sub_bbox, largura_caracteres=80, altura_caracteres=40):
    """
    Baixa o grafo de ruas do OSMnx e desenha as coordenadas em um 
    Canvas de 80x40 na memória RAM. Sem salvar arquivos, sem Matplotlib.
    """
    if not sub_bbox:
        return None
        
    norte, sul, leste, oeste = sub_bbox

    if norte == sul or leste == oeste:
        return None

    try:
        # CORREÇÃO DEFINITIVA: Tratamento da ordem das coordenadas
        try:
            # Padrão novo (OSMnx >= 2.0): bbox=(min_x, min_y, max_x, max_y)
            # Ou seja: (Oeste, Sul, Leste, Norte)
            G = ox.graph_from_bbox(bbox=(oeste, sul, leste, norte), network_type="all")
        except TypeError:
            # Padrão antigo (OSMnx < 2.0): north, south, east, west
            G = ox.graph_from_bbox(norte, sul, leste, oeste, network_type="all")
        
        if len(G) == 0:
            return None

        img = Image.new("L", (largura_caracteres, altura_caracteres), color=0)
        draw = ImageDraw.Draw(img)

        for u, v, data in G.edges(data=True):
            coordenadas = []
            
            if 'geometry' in data:
                xs, ys = data['geometry'].xy
                coordenadas = list(zip(xs, ys))
            else:
                x_u, y_u = G.nodes[u]['x'], G.nodes[u]['y']
                x_v, y_v = G.nodes[v]['x'], G.nodes[v]['y']
                coordenadas = [(x_u, y_u), (x_v, y_v)]

            pixels_linha = []
            for lon, lat in coordenadas:
                px = int(((lon - oeste) / (leste - oeste)) * largura_caracteres)
                py = int(((norte - lat) / (norte - sul)) * altura_caracteres)
                pixels_linha.append((px, py))
            
            draw.line(pixels_linha, fill=255, width=1)
        
        arte = conversor_ASCII(img)
        img.close()
        
        return arte

    except Exception as e:
        print(f" -> Erro técnico no quadrante: {e}")
        return None
        
        
def salvar_em_json(dicionario_mapas, arquivo_saida="mapas_gerados.json"):
    """
    Recebe um dicionário com chave = coordenada noroeste e valor = Arte ASCII,
    e salva o resultado formatado em um arquivo JSON.
    """
    # converte a tupla (lat, lon) do ponto mais a noroeste em uma string para o arquivo.
    dados_json = {str(chave): arte for chave, arte in dicionario_mapas.items()}
    
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(dados_json, f, ensure_ascii=False, indent=4)
        print(f"\nSucesso! {len(dados_json)} mapas foram salvos em '{arquivo_saida}'.")
    except Exception as e:
        print(f"\nErro ao salvar JSON: {e}")


# ==========================================
# FLUXO PRINCIPAL: INTEGRAÇÃO DOS DOIS MÉTODOS
# ==========================================
if __name__ == "__main__":
    print("=== GERADOR DE MAPAS ASCII ===")
    escolher_mapa = input("Para baixar os mapas da internet aperte 1. Para usar uma imagem local aperte 2: ")
    
    artes_geradas = {}
    
    if escolher_mapa == '1':
		#No momento a opção 1 não está funcionando, 
		#ou o servidor me bloqueou ou ele caiu.
        print("\n--- MODO 1: INTERNET (OSMnx) ---")
        # 1. Coleta de Dados Reais
        p1 = ler_coordenadas("Ponto Noroeste (Canto Superior Esquerdo)")
        p2 = ler_coordenadas("Ponto Sudeste (Canto Inferior Direito)")
        
        # 2. Definição da BBox Maior
        bbox_total = determinar_bbox_geral(p1, p2)
        
        # 3. Divisão em Grades
        grades = dividir_bbox_em_grade(bbox_total)
        
        # 4. Geração
        if grades:
            print(f"\nBBox dividida em {len(grades)} sub-grades. Baixando da internet...")
            for chave_noroeste, sub_bbox in grades.items():
                print(f"Processando Quadrante {chave_noroeste}...")
                mapa_em_caracteres = gerar_ascii_do_mapa(sub_bbox)
                
                if mapa_em_caracteres:
                    artes_geradas[chave_noroeste] = mapa_em_caracteres
                time.sleep(2) # Pausa amigável para não sobrecarregar a API
                
    elif escolher_mapa == '2':
        print("\n--- MODO 2: IMAGEM LOCAL (DADOS MOKADOS) ---")
        arquivo_mapa = input("Digite o nome exato da imagem (ex: mapa(3).png): ")
        
        # 1. Cria coordenadas fictícias para definir a área total (BBox Original)
        # Usando pontos mokados
        p1_mock = (0.0, 0.0)               # Latitude 0, Longitude 0 (Canto NW)
        p2_mock = (-0.005, 0.005)          # Deslocamento fictício (Canto SE)
        
        # 2. Definição da BBox Total Original
        bbox_total_mock = determinar_bbox_geral(p1_mock, p2_mock)
        
        # --- MODIFICAÇÃO AQUI ---
        # 3. sem a divisão em grade para não ser ncessário desenvolver um
        #sistema de coordenadas.
        # grades_mock = dividir_bbox_em_grade(bbox_total_mock) # Linha removida
        
        # 4. Geração de ÚNICA arte ASCII para o BBox Original
        if bbox_total_mock:
            print(f"\nProcessando BBox Original Completa a partir de (0.0, 0.0)...")
            
            # Definimos uma chave para o JSON (coordenada mais a Noroeste)
            chave_total = (bbox_total_mock[0], bbox_total_mock[3]) # (Norte, Oeste)
            
            # Chamamos a função de recorte passando o BBox Total nos dois campos de BBox.
            # Aumentamos as dimensões (ex: 120x60) para o mapa não ficar minúsculo,
            # já que não estamos mais somando vários pedaços de 80x40.
            mapa_em_caracteres = gerar_ascii_por_recorte(
                arquivo_mapa, 
                bbox_total_mock, # BBox de referência da imagem
                bbox_total_mock, # Área a ser recortada (a mesma da referência)
                largura_caracteres=80, # Largura maior para visão geral
                altura_caracteres=40     # Altura proporcional
            )
            
            if mapa_em_caracteres:
                artes_geradas[chave_total] = mapa_em_caracteres
                print("Arte ASCII gerada com sucesso para o BBox original.")
        # --- FIM DA MODIFICAÇÃO ---

    else:
        print("Opção inválida. Encerrando.")
        
    # ==========================================
    # SALVAMENTO FINAL (Serve para ambos os métodos)
    # ==========================================
    if artes_geradas:
        salvar_em_json(artes_geradas, "mapas_ascii.json")
    else:
        print("\nNenhum mapa pôde ser gerado. Verifique os erros acima.")
