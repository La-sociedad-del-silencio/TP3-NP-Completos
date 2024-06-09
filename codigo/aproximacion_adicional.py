from backtracking import caso_k_igual_a_n

def problema_tribu_del_agua_aprox_adicional(maestros_y_habilidades, k):
    n = len(maestros_y_habilidades)
    
    if k > n:
        return None

    if k == 0:
        return [], 0
    
    if k == n:
        return caso_k_igual_a_n(maestros_y_habilidades)

    S = [set() for _ in range(k)]
    
    maestros_y_habilidades = sorted(maestros_y_habilidades, key=lambda x: -x[1]) #O(n log n)

    grupo_actual = 0
    sumas = [0] * k
    for maestro_y_habilidad in maestros_y_habilidades: #O(n)
        if grupo_actual == k:
            grupo_actual = 0
             
        nombre, habilidad = maestro_y_habilidad
        
        S[grupo_actual].add(nombre)
        sumas[grupo_actual] += habilidad
        grupo_actual += 1

    coeficiente = sum(s**2 for s in sumas) #O(k)
    return S, coeficiente

# T(n) = O(n log n)
# Cota: 1.2157676348547717