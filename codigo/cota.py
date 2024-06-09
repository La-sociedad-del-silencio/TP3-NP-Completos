from aproximacion_adicional import problema_tribu_del_agua_aprox_adicional
    
def cota_aproximacion():
    cota_max = 1
    for caso in casos:
        maestros, k, coeficiente_esperado = caso
        S, coeficiente = problema_tribu_del_agua_aprox_adicional(maestros, k)
        razon = coeficiente / coeficiente_esperado
        if razon > cota_max:
            cota_max = razon
            
    return cota_max    
    
def caso_n_10():
    maestros = []
    for i in range(10):
        if i < 2:
            maestros.append((f'Maestro_{i}', 50))
        else:
            maestros.append((f'Maestro_{i}', 10))
    k = 3
    coeficiente_esperado = 10800
    return maestros, k, coeficiente_esperado

def caso_n_100():
    maestros = []
    for i in range(100):
        if i < 20:
            maestros.append((f'Maestro_{i}', 80))
        else:
            maestros.append((f'Maestro_{i}', 10))
    k = 30
    coeficiente_esperado = 192000
    return maestros, k, coeficiente_esperado

casos = [caso_n_10(), caso_n_100()]
    
print(cota_aproximacion()) 


    
