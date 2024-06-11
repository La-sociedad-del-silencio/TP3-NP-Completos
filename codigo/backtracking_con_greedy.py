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
    
    S_con_habilidades, coeficiente, _ = problema_tribu_del_agua_bt_greedy_recur(
        maestros_y_habilidades, 0, S, list(S), float('inf'), 
        sumas_grupos, float('inf'))

    resultado = obtener_resultado(S_con_habilidades)
        
    return resultado, coeficiente

def problema_tribu_del_agua_bt_greedy_recur(maestros_y_habilidades, 
    indice_actual, S_actual, mejor_S, mejor_suma, sumas_grupos, suma_maxima):
    
    if indice_actual == len(maestros_y_habilidades):
        suma_actual = sum(s ** 2 for s in sumas_grupos) 
        actual_suma_maxima = max(sumas_grupos)
        cota = min(actual_suma_maxima, suma_maxima)
        return list(map(set, S_actual)), suma_actual, cota
    
    S_actual, sumas_grupos = ordenar_por_suma(S_actual, sumas_grupos)
    maestro = maestros_y_habilidades[indice_actual]
    
    for i, grupo in enumerate(S_actual):
        grupo.add(maestro)
        sumas_grupos[i] += maestro[1]
        suma_actual = sum(s ** 2 for s in sumas_grupos) 
        explorado = False
        if suma_actual < mejor_suma and sumas_grupos[i] <= suma_maxima:
            explorado = True
            nuevo_S, nueva_suma , nueva_suma_maxima= problema_tribu_del_agua_bt_greedy_recur(
            maestros_y_habilidades, indice_actual+1, S_actual, mejor_S, 
            mejor_suma, sumas_grupos, suma_maxima)
            
            if nueva_suma < mejor_suma:
                mejor_S, mejor_suma, suma_maxima = nuevo_S, nueva_suma, nueva_suma_maxima
        sumas_grupos[i] -= maestro[1]
        grupo.remove(maestro)
        if not explorado:
            break
        
    return mejor_S, mejor_suma, suma_maxima

def ordenar_por_suma(S, sumas_grupos):
    grupos_con_sumas = list(zip(S, sumas_grupos))
    
    grupos_con_sumas.sort(key=lambda x: x[1])
    
    S, sumas_grupos = zip(*grupos_con_sumas)
    
    return list(S), list(sumas_grupos)