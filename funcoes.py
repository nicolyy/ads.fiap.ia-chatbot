def calcular_media_aritmetica(lista_numeros):
    if not lista_numeros:
        return None  # Retorna None se a lista estiver vazia
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

def calcular_media_geometrica(lista_numeros):
    if not lista_numeros:
        return None  # Retorna None se a lista estiver vazia
    produto = 1
    for numero in lista_numeros:
        produto *= numero
    media = produto ** (1 / len(lista_numeros))
    return media

def calcular_media_geometrica(numeros):
    if not numeros:
        return None  # Retorna None se a lista estiver vazia
    produto = 1
    for numero in numeros:
        produto *= numero
    media = produto ** (1 / len(numeros))
    return media