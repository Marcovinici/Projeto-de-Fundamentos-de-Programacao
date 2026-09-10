import osmnx as ox

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

    except Exception as e: # noqa: BLE001
        print(f" -> Erro técnico no quadrante: {e}")
        return None
 
