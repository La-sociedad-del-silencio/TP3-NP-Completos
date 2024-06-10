def problema_tribu_del_agua_bt(maestros_y_habilidades, k):
    n = len(maestros_y_habilidades)
    
    if k > n:
        return None
    
    if k == 0:
        return [], 0
    
    if k == n:
        return caso_k_igual_a_n(maestros_y_habilidades)
    
    S = [set() for _ in range(k)]
    maestros_y_habilidades = sorted(maestros_y_habilidades, 
                                    key=lambda x: -x[1])
    
    S_con_habilidades, coeficiente = problema_tribu_del_agua_bt_recur(
        maestros_y_habilidades, 0, S, list(S), float('inf'))
        
    resultado = obtener_resultado(S_con_habilidades)
        
    return resultado, coeficiente
            

def problema_tribu_del_agua_bt_recur(maestros_y_habilidades, 
    indice_actual, S_actual, mejor_S, mejor_suma):
    
    if indice_actual == len(maestros_y_habilidades):
        suma_actual = sumatoria(S_actual)
        return list(map(set, S_actual)), suma_actual
        
    for grupo in S_actual:
        grupo.add(maestros_y_habilidades[indice_actual])
        if sumatoria(S_actual) < mejor_suma:
            nuevo_S, nueva_suma = problema_tribu_del_agua_bt_recur(
                maestros_y_habilidades, indice_actual+1, S_actual, 
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

def caso_k_igual_a_n(maestros_y_habilidades):
    suma = 0
    grupos = []
    for maestro, habilidad in maestros_y_habilidades:
        grupos.append({maestro})
        suma += habilidad**2
    return grupos, suma

def obtener_resultado(S_con_habilidades):
    resultado = []
    
    for i in range(len(S_con_habilidades)):
        grupo = set()
        for maestro, _ in S_con_habilidades[i]:
            grupo.add(maestro)
        resultado.append(grupo)
        
    return resultado