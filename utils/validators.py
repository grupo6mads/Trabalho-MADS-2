def validar_nif(nif, restaurantes):

    if nif in restaurantes:
        return False, "NIF já existe"

    if len(nif) > 15:
        return False, "NIF inválido"

    return True, ""

def validar_preco(preco):

    return preco > 0

def validar_avaliacao(avaliacao):

    return avaliacao > 0

def validar_coordenadas(lat, lon):

    if not (-90 <= lat <= 90):
        return False

    if not (-180 <= lon <= 180):
        return False

    return True
