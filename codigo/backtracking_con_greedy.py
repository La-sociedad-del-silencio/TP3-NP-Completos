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
    sumas_grupos = {i: 0 for i in range(k)}
    
    mejor_S, mejor_suma, suma_maxima = asignacion_greedy(
                               maestros_y_habilidades, k)
    
    resultado = problema_tribu_del_agua_bt_greedy_recur(
        maestros_y_habilidades, 0, S, mejor_S, mejor_suma, 
        sumas_grupos, suma_maxima, 0, 0)
    
    S_resultado, coeficiente, _ = resultado
        
    return S_resultado, coeficiente

def problema_tribu_del_agua_bt_greedy_recur(maestros_y_habilidades, 
    indice_actual, S_actual, mejor_S, mejor_suma, sumas_grupos, 
    suma_maxima, suma_actual, actual_suma_maxima):
    
    if indice_actual == len(maestros_y_habilidades):
        cota = min(actual_suma_maxima, suma_maxima)
        return list(map(set, S_actual)), suma_actual, cota
    
    sumas_grupos_ordenada = sorted(sumas_grupos.items(), 
                             key=lambda item: item[1])    
    
    maestro, habilidad = maestros_y_habilidades[indice_actual]
    
    for suma_grupo in sumas_grupos_ordenada:
        i, _ = suma_grupo
        S_actual[i].add(maestro)
        sumas_grupos[i] += habilidad
        rama_explorada = False
        if sumas_grupos[i] <= suma_maxima:
            suma = sum(s ** 2 for s in sumas_grupos.values()) 
            if suma < mejor_suma:
                rama_explorada = True
                
                actual_suma_maxima = max(actual_suma_maxima, 
                                         sumas_grupos[i])
                
                resultado = problema_tribu_del_agua_bt_greedy_recur(
                maestros_y_habilidades, indice_actual+1, S_actual, 
                mejor_S, mejor_suma, sumas_grupos, suma_maxima,suma,
                actual_suma_maxima)

                nuevo_S, nueva_suma , nueva_suma_maxima = resultado

                if nueva_suma < mejor_suma:
                    mejor_S = nuevo_S
                    mejor_suma = nueva_suma
                    suma_maxima = nueva_suma_maxima 
        
        sumas_grupos[i] -= habilidad
        S_actual[i].remove(maestro)
        if not rama_explorada:
            break
        
    return mejor_S, mejor_suma, suma_maxima

def caso_k_igual_a_n(maestros_y_habilidades):
    suma = 0
    grupos = []
    for maestro, habilidad in maestros_y_habilidades:
        grupos.append({maestro})
        suma += habilidad**2
    return grupos, suma

def asignacion_greedy(maestros_y_habilidades, k):
    S = [set() for _ in range(k)]
    sumas_grupos = {i: 0 for i in range(k)}
    suma_maxima = 0
    
    for maestro_y_habilidad in maestros_y_habilidades:
        maestro, habilidad = maestro_y_habilidad
        grupo_menor_suma =  min(sumas_grupos, 
                                key=sumas_grupos.get) 
        S[grupo_menor_suma].add(maestro)
        sumas_grupos[grupo_menor_suma] += habilidad
        suma_maxima = max(suma_maxima, 
                          sumas_grupos[grupo_menor_suma])
        
    coeficiente = sum(s**2 for _,s in sumas_grupos.items())
    
    return S, coeficiente, suma_maxima 