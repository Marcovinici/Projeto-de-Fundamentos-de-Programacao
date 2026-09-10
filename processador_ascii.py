import json
import os

from PIL import Image

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
        
        for i, brilho in enumerate(pixels):
            # Áreas escuras abaixo do limiar viram espaço vazio (" ")
            if brilho < threshold:
                ascii_arte += " "
            # Áreas claras acima do limiar viram o caractere único (#)
            else:
                ascii_arte += caractere_branco
            
                
        return ascii_arte
    except  Exception: # noqa: BLE001
        print("Erro ao converter imagem para ASCII binário.")
        return

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
        
    except Exception as e: # noqa: BLE001
        print(f" -> Erro ao processar recorte da imagem: {e}")
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
    except Exception as e: # noqa: BLE001
        print(f"\nErro ao salvar JSON: {e}")

