def problema_tribu_del_agua_bt(maestros_y_habilidades, k):
    if k > len(maestros_y_habilidades):
        return None
    
    S = [set() for _ in range(k)]
    
    S_con_habilidades, coeficiente = problema_tribu_del_agua_bt_recur(maestros_y_habilidades, k, 0, list(S), list(S), float('inf'))

    resultado = []
    
    for i in range(len(S_con_habilidades)):
        grupo = set()
        for maestro, _ in S_con_habilidades[i]:
            grupo.add(maestro)
        resultado.append(grupo)
        
    return resultado, coeficiente
            

def problema_tribu_del_agua_bt_recur(maestros_y_habilidades, k, indice_actual, S_actual, mejor_S, mejor_suma):
    if indice_actual == len(maestros_y_habilidades):
        suma_actual = sumatoria(S_actual)
        if suma_actual < mejor_suma:
            return list(map(set, S_actual)), suma_actual
        return list(map(set, S_actual)), mejor_suma
        
    for grupo in S_actual:
        grupo.add(maestros_y_habilidades[indice_actual])
        if sumatoria(S_actual) < mejor_suma:
            nuevo_S, nueva_suma = problema_tribu_del_agua_bt_recur(maestros_y_habilidades, k, indice_actual+1, S_actual, mejor_S, mejor_suma)
            if nueva_suma < mejor_suma:
                mejor_S, mejor_suma = nuevo_S, nueva_suma
        grupo.remove(maestros_y_habilidades[indice_actual])
        
    return mejor_S, mejor_suma

def sumatoria(grupos):
    suma = 0
    for grupo in grupos:
        suma_grupo = 0
        for maestro, habilidad in grupo:
            suma_grupo += habilidad
        suma += suma_grupo ** 2
    return suma

k = 3
habilidades = [("Hasook", 120), ("Hama", 445), ("Senna", 546), ("Hama I", 222), ("Wei", 551), ("Wei I", 330)] 
        
#print(problema_tribu_del_agua_bt(habilidades, k))
""" 
Grupo 1: Wei, Hasook
Grupo 2: Senna, Hama I
Grupo 3: Hama, Wei I
Coeficiente: 1640690
"""
#10_3.txt
k = 3
h = [("Sangok", 178),("Wei", 121), ("Siku", 135), ("Eska", 168), ("Amon", 65), ("La", 37), ("Yue", 94), 
     ("Pakku", 91), ("Sura", 159), ("Tonraq", 27)]
""" 
Grupo 1: Sangok, Yue, Pakku - igual
Grupo 2: Eska, Wei, Amon - 354
Grupo 3: Sura, Siku, La, Tonraq - 358
Coeficiente: 385249
rta: ([{'Pakku', 'Sangok', 'Yue'}, {'La', 'Siku', 'Wei', 'Amon'}, {'Eska', 'Tonraq', 'Sura'}], 385249)
"""

#print(problema_tribu_del_agua_bt(h, k))