from aproximacion_catedra import problema_tribu_del_agua_aprox_catedra
import math
    
def cota_aproximacion():
    cota_max = 1
    for caso in casos:
        maestros, k, coeficiente_esperado = caso
        S, coeficiente = problema_tribu_del_agua_aprox_catedra(maestros, k)
        print(coeficiente_esperado, coeficiente)
        razon = coeficiente / coeficiente_esperado
        if razon > cota_max:
            print(f'peor cota = {razon} con n = {len(maestros)}')
            cota_max = razon
            
    return cota_max    


def caso_n_10():
    maestros = [("M1", 5000), ("M2", 5000), ("M3", 4000), ("M4", 3999), ("M5", 3999), 
                ("M6", 100), ("M7", 100), ("M8", 100), ("M9", 100), ("M10", 100)]
    k = 2
    coeficiente_esperado = (5000 + 5000 + 100 * 5)**2 + (4000 + 3999*2)**2
    return maestros, k, coeficiente_esperado

def caso_n_100():

    maestros = [("M1", 6000), ("M2", 5999), ("M3", 5999)]
    k = 2
    for i in range(4, 99):
        maestros.append((f"M{i}", 10))
    maestros.append((("M99"), 8250))
    maestros.append((("M100"), 8250))
    coeficiente_esperado = (8250 * 2 + 95 * 10)**2 + (6000 + 5999*2)**2 
    return maestros, k, coeficiente_esperado

def caso_n_1000():

    maestros = [("M1", 10000), ("M2", 9999), ("M3", 9999)]
    k = 2
    for i in range(4, 999):
        maestros.append((f"M{i}", 1))
    maestros.append((("M999"), 14501))
    maestros.append((("M1000"), 14501))
    #print(sum(s[1] for s in maestros))
    coeficiente_esperado = (14501 * 2 + 995 )**2 + (10000 + 9999*2)**2 
    return maestros, k, coeficiente_esperado


def caso_n_10000():

    maestros = [("M1", 500000), ("M2", 499999), ("M3", 499999)]
    k = 2
    for i in range(4, 9999):
        maestros.append((f"M{i}", 2))
    maestros.append((("M999"), 740004))
    maestros.append((("M1000"), 740004))
    #print(sum(s[1] for s in maestros)) 
    coeficiente_esperado = (740004 * 2 + 9995 *2 )**2 + (500000 + 499999*2)**2 
    return maestros, k, coeficiente_esperado 

casos = [caso_n_10(), caso_n_100(), caso_n_1000(), caso_n_10000()]

#print(cota_aproximacion())
#1.0256009216095232
