def aproximacion_propuesta(maestros_y_habilidades, k):
    if k > len(maestros_y_habilidades):
        return None

    if k == 0:
        return [], 0

    S = [set() for _ in range(k)]
    maestros_y_habilidades = sorted(maestros_y_habilidades, key=lambda x: -x[1]) #O(n log n)

    for maestro_y_habilidad in maestros_y_habilidades: #O(n * k)
        if k == 1:
            S[0].add(maestro_y_habilidad)
            continue
        grupo_con_menor_habilidad = 0
        menor_cuadrado_suma = sum(S[0])**2
        for i in range(1, k): #O(k)
            cuadrado_suma = sum(S[i])**2
            if cuadrado_suma < menor_cuadrado_suma:
                menor_cuadrado_suma = cuadrado_suma
                grupo_con_menor_habilidad = i
        S[grupo_con_menor_habilidad].add(maestro_y_habilidad)

    resultado = []
    coeficiente = 0
    for grupo_con_habilidades in S: #O(k * n)
        grupo = set()
        cuadrado_suma = 0
        for maestro, habilidad in grupo_con_habilidades:
            grupo.add(maestro)
            cuadrado_suma += habilidad
        coeficiente += cuadrado_suma**2
        resultado.append(grupo)

    return resultado, coeficiente

# T(n) = 2 * O(n * k) + O(n log n) En el peor caso n~k y T(n) = O(n * k) (puede llegar a ser cuadrático) 
