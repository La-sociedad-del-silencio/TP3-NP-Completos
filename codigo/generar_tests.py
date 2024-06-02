from random import randint
from backtracking import problema_tribu_del_agua_bt
from grafico_complejidad import *

def obtener_maestros():
    maestros_sin_repetidos = []
    
    with open("ejemplos_catedra/Resultados_Esperados.txt", "r") as f:
        
        for linea in f:
            linea = linea.strip()
            
            if linea.startswith('Grupo'):
                grupo = linea.split(': ')[1]
                maestros = grupo.split(", ")
                for maestro in maestros:
                    if maestro not in maestros_sin_repetidos:
                        maestros_sin_repetidos.append(maestro)

    return maestros_sin_repetidos 
    
def escribir_test(nombre_archivo, k, maestros, coeficiente, grupos):
    
    with open(f'ejemplos_adicionales/{nombre_archivo}', "w") as f:
        f.write(f'{k}\n')
        for maestro in maestros:
            nombre, habilidad = maestro
            f.write(f'{nombre}, {habilidad}\n')
            
    with open("ejemplos_adicionales/Resultados_Esperados.txt", "a") as f:
        f.write(f'{nombre_archivo}\n')
        for i, grupo in enumerate(grupos):
            f.write(f'Grupo {i+1}: {", ".join(grupo)}\n')
        f.write(f"Coeficiente: {coeficiente}\n\n")
        
def caso_uno_por_grupo():
    maestros_y_habilidades = generar_test(5)
    k = 5
    
    coeficiente = 0
    grupos = []
    for maestro, habilidad in maestros_y_habilidades:
        coeficiente += habilidad**2
        grupos.append({maestro})
    escribir_test("uno_por_grupo.txt", k, maestros_y_habilidades, coeficiente, grupos)
    
def caso_habilidades_parejas():
    nombres_maestros = MAESTROS
    maestros_y_habilidades = []
    
    habilidad_actual = 100
    k = 2
    grupos = [set() for _ in range(k)] 
    for i in range(6):
        habilidad = habilidad_actual
        if habilidad in {100, 103, 105}: # hay varias combinaciones que dan igual coeficiente
            grupos[0].add(nombres_maestros[i])
        else:
            grupos[1].add(nombres_maestros[i])
        maestros_y_habilidades.append((nombres_maestros[i], habilidad))
        habilidad_actual += 1
    
    coeficiente = 189113
    
    escribir_test("habilidades_parejas.txt", k, maestros_y_habilidades, coeficiente, grupos)    

def caso_grupos_parejos():
    nombres_maestros = MAESTROS
    maestros_y_habilidades = []
    
    habilidad_baja = 100
    habilidad_alta = 700
    k = 3
    grupos = [set() for _ in range(k)] 
    grupo_actual = 0
    for i in range(6):
        habilidad = None
        if i <= 2:
            habilidad = habilidad_baja
            grupos[grupo_actual].add(nombres_maestros[i])
            habilidad_baja += 1
            grupo_actual += 1
        else:
            grupo_actual -= 1
            habilidad = habilidad_alta
            grupos[grupo_actual].add(nombres_maestros[i])
            habilidad_alta += 1
        maestros_y_habilidades.append((nombres_maestros[i], habilidad))
        
    
    coeficiente = 1929612
    
    escribir_test("grupos_parejos.txt", k, maestros_y_habilidades, coeficiente, grupos)    

caso_grupos_parejos()