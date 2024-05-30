def validador_problema_tribu_del_agua(habilidades_maestros_agua, k, B, S):
    if len(S) != k: #O(1)
        return False 
    suma = 0 #O(1)
    maestros = set() #O(1) Cada maestro debe estar en solo un grupo
    dic_habilidades = dict() #O(1)
    
    for info_maestro in habilidades_maestros_agua: #O(n)
        maestro, habilidad = info_maestro #O(1)
        dic_habilidades[maestro] = habilidad #O(1)
    
    # O(n * k)
    for grupo in S: # k grupos: O(k)
        suma_grupo = 0 #O(1)
        for maestro in grupo: # En el peor caso O(n)
            if maestro in maestros or maestro not in dic_habilidades:
                return False # El maestro dado está en más de un grupo
            maestros.add(maestro) #O(1)
            suma_grupo += dic_habilidades[maestro] #O(1)
        suma += suma_grupo ** 2 #O(1)
            
    if suma > B:  # O(1)
        return False
        
    for maestro, _habilidad in habilidades_maestros_agua: #O(n)
        if maestro not in maestros:  # O(1)
            return False # No tiene grupo asignado
        
    return True
    
# T(n) = O(1) + O(k * n) + 2*O(n) = O(k * n). En el peor caso k=n (1 maestro por grupo) y sería O(n^2)
        
k = 3
habilidades = [("Hasook", 120), ("Hama", 445), ("Senna", 546), ("Hama I", 222), ("Wei", 551), ("Wei I", 330)] 
S = [{"Wei", "Hasook"}, {"Senna", "Hama I"}, {"Hama", "Wei I"}]
B = 1640690

print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # True: Suma == B

B = 1640691
print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # True: Suma > B

B = 1640689
print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # False: Suma < B

S[2].remove("Hama")
print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # False: un maestro no tiene grupo

S[2].add("Hama")
S[2].add("Wei")
print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # False: un maestro tiene más de un grupo

S.pop()
print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # False: hay menos de k grupos

S = [{"Wei", "Hasook"}, {"Senna", "Hama I"}, {"Hama", "Wei I"}, {"Infiltrado"}]
print(validador_problema_tribu_del_agua(habilidades, k, B, S)) # False: hay más de k grupos
