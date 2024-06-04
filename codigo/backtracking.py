def problema_tribu_del_agua_bt(maestros_y_habilidades, k):
    if k > len(maestros_y_habilidades):
        return None
    
    if k == 0:
        return [], 0
    
    S = [set() for _ in range(k)]
    maestros_y_habilidades = sorted(maestros_y_habilidades, 
                                    key=lambda x: -x[1])
    S_con_habilidades, coeficiente = problema_tribu_del_agua_bt_recur(
        maestros_y_habilidades, k, 0, list(S), list(S), float('inf'))

    resultado = []
    
    for i in range(len(S_con_habilidades)):
        grupo = set()
        for maestro, _ in S_con_habilidades[i]:
            grupo.add(maestro)
        resultado.append(grupo)
        
    return resultado, coeficiente
            

def problema_tribu_del_agua_bt_recur(maestros_y_habilidades, 
    k, indice_actual, S_actual, mejor_S, mejor_suma):
    
    if indice_actual == len(maestros_y_habilidades):
        suma_actual = sumatoria(S_actual)
        if suma_actual < mejor_suma:
            return list(map(set, S_actual)), suma_actual
        return list(map(set, S_actual)), mejor_suma
        
    for grupo in S_actual:
        grupo.add(maestros_y_habilidades[indice_actual])
        if sumatoria(S_actual) < mejor_suma:
            nuevo_S, nueva_suma = problema_tribu_del_agua_bt_recur(
                maestros_y_habilidades, k, indice_actual+1, S_actual, 
                mejor_S, mejor_suma)
            
            if nueva_suma < mejor_suma:
                mejor_S, mejor_suma = nuevo_S, nueva_suma
        grupo.remove(maestros_y_habilidades[indice_actual])
        
    return mejor_S, mejor_suma

def sumatoria(grupos):
    suma = 0
    for grupo in grupos:
        suma_grupo = 0
        for _maestro, habilidad in grupo:
            suma_grupo += habilidad
        suma += suma_grupo ** 2
    return suma
