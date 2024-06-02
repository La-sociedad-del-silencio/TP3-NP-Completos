def validador_2_partition(valores, s1, s2):
    if sum(s1) != sum(s2) or len(s1) >= len(valores) or len(s2) >= len(valores):
        return False
    
    apariciones = {}
    for elemento in s1:
        apariciones[elemento] = apariciones.get(elemento, 0) + 1
        
    for elemento in s2:
        apariciones[elemento] = apariciones.get(elemento, 0) + 1
        
    valores_no_repetidos = {}
    for valor in valores:
        nuevoValor = valores_no_repetidos.get(valor, 0) + 1
        valores_no_repetidos[valor] = nuevoValor
        
    if len(apariciones) != len(valores_no_repetidos):
        return False
    
    for valor, cantidad in apariciones:
        if valor not in valores_no_repetidos:
            return False
        elif valores_no_repetidos[valor] != cantidad:
            return False
        
    return True        
