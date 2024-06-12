def problema_tribu_del_agua_aprox_catedra(maestros_y_habilidades, k):
    if k > len(maestros_y_habilidades):
        return None

    if k == 0:
        return [], 0

    S = [set() for _ in range(k)]
    maestros_y_habilidades = sorted(maestros_y_habilidades, key=lambda x: -x[1]) #O(n log n)
    sumas_grupos = {i: 0 for i in range(k)}
    
    for maestro_y_habilidad in maestros_y_habilidades:
        maestro, habilidad = maestro_y_habilidad
        grupo_menor_suma =  min(sumas_grupos, 
                                key=sumas_grupos.get) 
        S[grupo_menor_suma].add(maestro)
        sumas_grupos[grupo_menor_suma] += habilidad
                
    coeficiente = sum(s**2 for _,s in sumas_grupos.items())
    
    return S, coeficiente

# T(n) = 2 * O(n * k) + O(n log n) En el peor caso n~k y T(n) = O(n * k) (puede llegar a ser cuadrático) 
