from backtracking import caso_k_igual_a_n

def problema_tribu_del_agua_aprox_catedra(maestros_y_habilidades, k):
    n = len(maestros_y_habilidades)
    
    if k > n:
        return None

    if k == 0:
        return [], 0
    
    if k == n:
        return caso_k_igual_a_n(maestros_y_habilidades)

    S = [set() for _ in range(k)]
    maestros_y_habilidades = sorted(maestros_y_habilidades, key=lambda x: -x[1]) #O(n log n)
    sumas_grupos = {i: 0 for i in range(k)}
    
    for maestro_y_habilidad in maestros_y_habilidades:
        maestro, habilidad = maestro_y_habilidad
        grupo_menos_habilidoso =  min(sumas_grupos, 
                                    key=lambda x: sumas_grupos[x]**2) 
        S[grupo_menos_habilidoso].add(maestro)
        sumas_grupos[grupo_menos_habilidoso] += habilidad
                
    coeficiente = sum(s**2 for _,s in sumas_grupos.items())
    
    return S, coeficiente

# T(n) = 2 * O(n * k) + O(n log n) En el peor caso n~k y T(n) = O(n * k) (puede llegar a ser cuadrático) 
