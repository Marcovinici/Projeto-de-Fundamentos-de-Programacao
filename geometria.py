import math

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
    except ValueError as e:
        print(f"Erro ao determinar BBox: {e}")
        return

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


