from aproximacion_adicional import problema_tribu_del_agua_aprox_adicional
    
def cota_aproximacion():
    cota_max = 1
    for caso in casos:
        maestros, k, coeficiente_esperado = caso
        S, coeficiente = problema_tribu_del_agua_aprox_adicional(maestros, k)
        print(coeficiente_esperado, coeficiente)
        razon = coeficiente / coeficiente_esperado
        if razon > cota_max:
            print(f'peor cota: {len(maestros)}')
            cota_max = razon
            
    return cota_max    
    
def caso_n_10():
    maestros = [(f'Maestro_{i}', 50 if i < 2 else 10) for i in range(10)]
    k = 3
    coeficiente_esperado = 2 * (50 + 10)**2 + (6 * 10)**2  # 10800
    return maestros, k, coeficiente_esperado

def caso_n_100():
    maestros = [(f'Maestro_{i}', 80 if i < 20 else 10) for i in range(100)]
    k = 30
    coeficiente_esperado = 20 * (80)**2 + 10 * (8 * 10)**2  # 192000
    return maestros, k, coeficiente_esperado

def caso_n_500():
    maestros = [(f'Maestro_{i}', 80 if i < 200 else 40) for i in range(500)]
    k = 350
    coeficiente_esperado = 200 * (80)**2 + 150 * (80)**2  # 2240000
    return maestros, k, coeficiente_esperado

def caso_n_1000():
    maestros = [(f'Maestro_{i}', 1000 if i < 900 else 10) for i in range(1000)]
    k = 901
    coeficiente_esperado = 900 * (1000)**2 + (100 * 10)**2  # 901000000
    return maestros, k, coeficiente_esperado

def caso_n_1500():
    maestros = [(f'Maestro_{i}', 100 if i < 700 else 50 if i < 1200 else 20) for i in range(1500)]
    # 700 de 100, 500 de 50, 300 de 20
    k = 1010
    coeficiente_esperado = 700 * (100)**2 + 250 * (50 * 2)**2 + 60 * (20 * 5)**2  # 10100000
    return maestros, k, coeficiente_esperado

def caso_n_2000():
    maestros = [(f'Maestro_{i}', 90 if i < 800 else 60 if i < 1400 else 30) for i in range(2000)]
    #800 de 90, 600 de 60 y 30
    k = 1400
    coeficiente_esperado = 800 * (90)**2 + 600 * (60 + 30)**2  # 11340000
    return maestros, k, coeficiente_esperado

def caso_n_2000_2():
    maestros = [(f'Maestro_{i}', 90 if i < 800 else 60 if i < 1400 else 30) for i in range(2000)]
    #800 de 90, 600 de 60 y 30
    k = 1400
    coeficiente_esperado = 600 * (90 + 60)**2 + 200 * (90 + 30 + 30)**2 + 40*(5*30)**2  # 18900000
    return maestros, k, coeficiente_esperado

def caso_n_2000_3():
    maestros = [(f'Maestro_{i}', 100 if i < 400 else 50) for i in range(2000)]
    k = 1200
    coeficiente_esperado = 400 * (100)**2 + 800 * (2*50)**2  # 12000000
    return maestros, k, coeficiente_esperado

def caso_n_2000_4():
    maestros = [(f'Maestro_{i}', 100 if i < 400 else 80) for i in range(2000)]
    k = 1200
    coeficiente_esperado = 400 * (100)**2 + 800 * (2*80)**2  # 24480000 vs 25760000
    return maestros, k, coeficiente_esperado

def caso_n_2500():
    maestros = [(f'Maestro_{i}', 110 if i < 1000 else 70 if i < 2000 else 40) for i in range(2500)]
    # 1000 de 110, 1000 de 70 y 500 de 40
    k = 2000
    coeficiente_esperado = 1000 * (110)**2 + 500 * (70 + 40)**2 + 500 * (70)**2  # 20600000
    return maestros, k, coeficiente_esperado

def caso_n_5000():
    maestros = [(f'Maestro_{i}', 4000 if i < 1 else 10) for i in range(5000)]
    # 1 de 4000, 4999 de 10
    k = 2
    coeficiente_esperado = (4000 + 10 * 2299)**2 + (10 * 2700)**2  # 1457460100
    return maestros, k, coeficiente_esperado

def caso_n_10000():
    maestros = [(f'Maestro_{i}', 80 if i < 2000 else 40) for i in range(10000)]
    k = 6000
    coeficiente_esperado = 2000 * (80)**2 + 4000 * (2*40)**2  # 38400000
    return maestros, k, coeficiente_esperado

def caso_n_10000_2():
    maestros = [(f'Maestro_{i}', 100000 if i < 1 else 10) for i in range(10000)]
    k = 2
    coeficiente_esperado = (100000)**2 + (10 * 9999)**2  # 19998000100
    return maestros, k, coeficiente_esperado

def caso_n_100000():
    maestros = [(f'Maestro_{i}', 200000 if i < 1 else 1) for i in range(100000)]
    k = 2
    coeficiente_esperado = (200000)**2 + (1 * 99999)**2  # 49999800001
    return maestros, k, coeficiente_esperado

def caso_n_100000_2():
    maestros = [(f'Maestro_{i}', 2000000 if i < 1 else 20) for i in range(100000)]
    k = 2
    coeficiente_esperado = (2000000)**2 + (20 * 99999)**2  # 7999920000400
    return maestros, k, coeficiente_esperado

casos = [caso_n_10(), caso_n_100(), caso_n_500(), caso_n_1000(), caso_n_1500(), 
        caso_n_2000(), caso_n_2000_2(), caso_n_2000_3(), caso_n_2000_4(), 
        caso_n_2500(), caso_n_5000(), caso_n_10000(), caso_n_10000_2(),
        caso_n_100000(), caso_n_100000_2()]
    
#print(cota_aproximacion()) 
#1.2999951999748 