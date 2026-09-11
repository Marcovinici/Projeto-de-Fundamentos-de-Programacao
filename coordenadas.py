import time

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
        
        coordenadas = (str_lat, str_lon)
        coordenadas = processar_coordenadas(coordenadas)
        
        if coordenadas == None:
            break
    return coordenadas
        
def processar_coordenadas(coordenadas):
    str_lat, str_lon = coordenadas
    try:
        partes_lat = separar_dms(str_lat)
        partes_lon = separar_dms(str_lon)
           
        latitude_decimal = converter_para_decimal(*partes_lat)
        longitude_decimal = converter_para_decimal(*partes_lon)

        return (latitude_decimal, longitude_decimal)     
    except ValueError:  
        print("As coordenadas foram mal definidas. Tente novamente.")
        time.sleep(3) # Pausa por 3 segundos antes de recomeçar o loop
    finally:
        pass
