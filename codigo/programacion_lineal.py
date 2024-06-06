import pulp

def problema_tribu_del_agua_pl(maestros_y_habilidades, k):
    num_maestros = len(maestros_y_habilidades)
    
    X = pulp.LpVariable.dicts("X", ((i, j) for i in range(num_maestros) for j in range(k)), cat='Binary')
    
    # suma de cada grupo
    S = [pulp.lpSum(maestros_y_habilidades[i][1] * X[i, j] for i in range(num_maestros)) for j in range(k)]

    # S_max = Z, S_min = Y
    S_max = pulp.LpVariable("S_max", lowBound=0, cat='Continuous')
    S_min = pulp.LpVariable("S_min", lowBound=0, cat='Continuous')

    problem = pulp.LpProblem("Problema_Tribu_del_Agua_con_PL", pulp.LpMinimize)

    # Función objetivo: minimizar la diferencia entre el grupo con mayor habilidad y el grupo con menor habilidad
    problem += S_max - S_min
    
    # Restricciones para S_max y S_min
    # S_max debe ser mayor o igual a todas las sumas
    # S_min debe ser menor o igual a todas las sumas
    for j in range(k):
        problem += S_max >= S[j]
        problem += S_min <= S[j]

    # Restricciones para las asignaciones: cada maestro debe ser asignado a exactamente un grupo
    for i in range(num_maestros):
        problem += pulp.lpSum(X[i, j] for j in range(k)) == 1

    problem.solve(pulp.PULP_CBC_CMD(msg=False))
    
    # Extraer la solución
    #resultado = [[(i, maestros_y_habilidades[i][1]) for i in range(n) if pulp.value(X[i, j]) == 1] for j in range(k)]
    #coeficiente = pulp.value(prob.objective)
    
    resultado = [set() for _ in range(k)]
    suma_por_grupo = [0 for _ in range(k)]
    
    for i in range(num_maestros):
        for grupo in range(k):
            if pulp.value(X[i, grupo]) == 1:
                resultado[grupo].add(maestros_y_habilidades[i][0])
                suma_por_grupo[grupo] += maestros_y_habilidades[i][1]
                
    coeficiente = sum(s**2 for s in suma_por_grupo)
    
    
    return resultado, coeficiente

# Datos de prueba
k = 3
habilidades = [("Hasook", 120), ("Hama", 445), ("Senna", 546), ("Hama I", 222), ("Wei", 551), ("Wei I", 330)]

#print(problema_tribu_del_agua_pl(habilidades, k))
