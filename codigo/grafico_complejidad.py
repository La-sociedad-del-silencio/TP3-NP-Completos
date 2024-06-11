from random import randint
import time

from backtracking_con_greedy import *

import matplotlib.pyplot as plt

MAESTROS = ['Yakone', 'Yue', 'Pakku', 'Wei', 'Pakku I', 'Hasook', 'Senna', 'Hama I', 'Hama', 'Wei I', 'Huu', 'Eska', 'Sura', 'Sangok', 'Ming-Hua', 'Katara', 'Rafa', 'Unalaq', 'Amon', 'Tonraq', 'Misu', 'Siku', 'La', 'Siku I', 'Desna', 'Desna I', 'Tho', 'Kya', 'Siku II', 'Misu I', 'Kuruk', 'Eska I', 'Tonraq I', 'Eska II', 'Sangok I', 'Huu I', 'Huu II', 'Kya I', 'Ming-Hua I', 'Kuruk I', 'Senna II', 'Senna I', 'Hasook I', 'Yakone I', 'Amon I', 'Pakku II', 'Yue I', 'Yue II', 'Amon II', 'Tho I', 'Rafa I', 'Sura I', 'Sangok II', 'Misu II', 'Huu III']


def generar_test(cantidad):
    nombres_maestros = MAESTROS
    maestros_y_habilidades = []
    
    for i in range(cantidad):
        habilidad = randint(50, 1000)
        maestros_y_habilidades.append((nombres_maestros[i], habilidad))
        
    return maestros_y_habilidades 

def generar_tests_y_graficar(titulo, algoritmo, nombre_imagen):
    max_val = 11

    iter = 1
    total_iters = 66
    
    cantidad_maestros = [i for i in range(max_val)]
    valores_k_usados = []
    tiempos = []
    
    for i in range(max_val):
        mayor_tiempo = 0
        mayor_k = 0
        maestros_y_habilidades = generar_test(i)
        for k in range(min(max_val, i) + 1):  
            print(f"Iteracion {iter}/{total_iters}")
            ms_que_llevo = correrTest(i, k, maestros_y_habilidades, algoritmo)
            if mayor_tiempo < ms_que_llevo:
                mayor_tiempo = ms_que_llevo
                mayor_k = k
            iter += 1
        valores_k_usados.append(mayor_k)
        tiempos.append(mayor_tiempo)
    
    plt.figure(figsize=(12, 7))
    fig, ax = plt.subplots()
    plt.plot(cantidad_maestros, tiempos, color='red')
    
    
    xticks_labels = [f'n={n}, k={k}' for n, k in zip(cantidad_maestros, valores_k_usados)]
    ax.set_xticks(cantidad_maestros)
    ax.set_xticklabels(xticks_labels, rotation=45, ha='right')
    ax.set_xlabel('Número de maestros (n) con el valor de k \nque tuvo el mayor tiempo de ejecución')
    ax.set_ylabel('Tiempo de ejecución (ms)\n')
    ax.set_title(f'{titulo}: Tiempos de ejecución para \ndiferentes valores de n y k')
    plt.tight_layout()
    plt.savefig(f'images/{nombre_imagen}.png', format="png")
    plt.show()

        
def correrTest(n, k, maestros_y_habilidades, algoritmo):
    inicio = time.time()

    resultado = algoritmo(maestros_y_habilidades, k)
    fin = time.time()

    msQueLlevo = int((fin - inicio) * 1000)

    if resultado is not None:
        grupos, coeficiente = resultado
        # Solo ejecutar la primera vez
        #escribir_test("./ejemplos_mediciones", f"{n}_{k}.txt", k, maestros_y_habilidades, coeficiente, grupos, msQueLlevo)
    
    return msQueLlevo

def escribir_test(carpeta, nombre_archivo, k, maestros, coeficiente, grupos, tiempo_ejecucion):
    
    with open(f'{carpeta}/{nombre_archivo}', "w") as f:
        f.write(f'{k}\n')
        for maestro in maestros:
            nombre, habilidad = maestro
            f.write(f'{nombre}, {habilidad}\n')
            
    with open(f"{carpeta}/Resultados_Esperados.txt", "a") as f:
        f.write(f'{nombre_archivo}\n')
        for i, grupo in enumerate(grupos):
            f.write(f'Grupo {i+1}: {", ".join(grupo)}\n')
        if tiempo_ejecucion is not None:
            f.write(f'Tiempo de ejecucion: {tiempo_ejecucion} ms\n')
        f.write(f"Coeficiente: {coeficiente}\n\n")