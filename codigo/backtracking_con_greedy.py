from backtracking import caso_k_igual_a_n, obtener_resultado

def problema_tribu_del_agua_bt_greedy(maestros_y_habilidades, k):
    n = len(maestros_y_habilidades)
    
    if k > n:
        return None
    
    if k == 0:
        return [], 0
    
    if k == n:
        return caso_k_igual_a_n(maestros_y_habilidades)        

    maestros_y_habilidades = sorted(maestros_y_habilidades, 
                                    key=lambda x: -x[1])

    S = [set() for _ in range(k)]
    sumas_grupos = [0] * k #O(k)
    
    S_con_habilidades, coeficiente = problema_tribu_del_agua_bt_greedy_recur(
        maestros_y_habilidades, 0, list(S), list(S), float('inf'), 
        sumas_grupos)

    resultado = obtener_resultado(S_con_habilidades)
        
    return resultado, coeficiente

def problema_tribu_del_agua_bt_greedy_recur(maestros_y_habilidades, 
    indice_actual, S_actual, mejor_S, mejor_suma, sumas_grupos):
    
    if indice_actual == len(maestros_y_habilidades):
        suma_actual = sum(s ** 2 for s in sumas_grupos) 
        if suma_actual < mejor_suma:
            return list(map(set, S_actual)), suma_actual
        return list(map(set, S_actual)), mejor_suma
    
    S_actual, sumas_grupos = ordenar_por_suma(S_actual, sumas_grupos)
    maestro = maestros_y_habilidades[indice_actual]
    
    for i, grupo in enumerate(S_actual):
        grupo.add(maestro)
        sumas_grupos[i] += maestro[1]
        suma_actual = sum(s ** 2 for s in sumas_grupos) 
        if suma_actual < mejor_suma:
            nuevo_S, nueva_suma = problema_tribu_del_agua_bt_greedy_recur(
            maestros_y_habilidades, indice_actual+1, S_actual, mejor_S, 
            mejor_suma, sumas_grupos)
            
            if nueva_suma < mejor_suma:
                mejor_S, mejor_suma = nuevo_S, nueva_suma
        sumas_grupos[i] -= maestro[1]
        grupo.remove(maestro)
        
    return mejor_S, mejor_suma

def ordenar_por_suma(S, sumas_grupos):
    grupos_con_sumas = list(zip(S, sumas_grupos))
    
    grupos_con_sumas.sort(key=lambda x: x[1])
    
    S, sumas_grupos = zip(*grupos_con_sumas)
    
    return list(S), list(sumas_grupos)