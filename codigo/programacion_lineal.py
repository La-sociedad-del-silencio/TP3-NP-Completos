import pulp
from backtracking_con_greedy import caso_k_igual_a_n

def problema_tribu_del_agua_pl(maestros_y_habilidades, k):
    num_maestros = len(maestros_y_habilidades)
    
    if k > num_maestros:
        return None
    
    if k == 0:
        return [], 0
    
    if k == num_maestros:
        return caso_k_igual_a_n(maestros_y_habilidades)
    
    # variables
    X = pulp.LpVariable.dicts("X", ((i, j) 
    for i in range(num_maestros) for j in range(k)), cat='Binary')
    
    # suma de cada grupo
    S = [pulp.lpSum(maestros_y_habilidades[i][1] * X[i, j] 
        for i in range(num_maestros)) for j in range(k)]

    # Variables: S_max = Z, S_min = Y
    S_max = pulp.LpVariable("S_max", lowBound=0, cat='Integer')
    S_min = pulp.LpVariable("S_min", lowBound=0, cat='Integer')

    problem = pulp.LpProblem("Problema_Tribu_del_Agua_con_PL", 
                             pulp.LpMinimize)
    
    # Restricciones para las asignaciones: cada maestro debe 
    # ser asignado a exactamente un grupo
    for i in range(num_maestros):
        problem += pulp.lpSum(X[i, j] for j in range(k)) == 1
    
    # Restricciones para S_max y S_min
    # S_max debe ser mayor o igual a todas las sumas
    # S_min debe ser menor o igual a todas las sumas
    for j in range(k):
        problem += S_max >= S[j]
        problem += S_min <= S[j]
        
    # Función objetivo: minimizar la diferencia entre el grupo 
    # con mayor habilidad y el grupo con menor habilidad
    problem += S_max - S_min

    # Resolver
    problem.solve(pulp.PULP_CBC_CMD(msg=False))
    
    return obtener_resultado(num_maestros, k, 
                            maestros_y_habilidades, X)

def obtener_resultado(num_maestros, k, maestros_y_habilidades, X):
    resultado = [set() for _ in range(k)]
    suma_por_grupo = [0 for _ in range(k)]
    
    for i in range(num_maestros):
        for grupo in range(k):
            if pulp.value(X[i, grupo]) == 1:
                nombre = maestros_y_habilidades[i][0]
                habilidad = maestros_y_habilidades[i][1]
                resultado[grupo].add(nombre)
                suma_por_grupo[grupo] += habilidad
                
    coeficiente = sum(s**2 for s in suma_por_grupo) 
    return resultado, coeficiente

# Cota set de ej adicionales: 1 
# Cota set de mediciones: 1.0141856654211776
# Cota set de la cátedra: