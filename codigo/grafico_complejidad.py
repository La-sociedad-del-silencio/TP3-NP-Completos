from random import randint
import time

from backtracking import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

MAESTROS = ['Yakone', 'Yue', 'Pakku', 'Wei', 'Pakku I', 'Hasook', 'Senna', 'Hama I', 'Hama', 'Wei I', 'Huu', 'Eska', 'Sura', 'Sangok', 'Ming-Hua', 'Katara', 'Rafa', 'Unalaq', 'Amon', 'Tonraq', 'Misu', 'Siku', 'La', 'Siku I', 'Desna', 'Desna I', 'Tho', 'Kya', 'Siku II', 'Misu I', 'Kuruk', 'Eska I', 'Tonraq I', 'Eska II', 'Sangok I', 'Huu I', 'Huu II', 'Kya I', 'Ming-Hua I', 'Kuruk I', 'Senna II', 'Senna I', 'Hasook I', 'Yakone I', 'Amon I', 'Pakku II', 'Yue I', 'Yue II', 'Amon II', 'Tho I', 'Rafa I', 'Sura I', 'Sangok II', 'Misu II', 'Huu III']


def generar_test(cantidad):
    nombres_maestros = MAESTROS
    maestros_y_habilidades = []
    
    for i in range(cantidad):
        habilidad = randint(50, 1000)
        maestros_y_habilidades.append((nombres_maestros[i], habilidad))
        
    return maestros_y_habilidades 

def generar_tests_y_graficar():
    max_val = 51

    iter = 1
    total_iters = 10 * max_val
    
    cantidad_maestros = [i for i in range(max_val)]
    tiempos = []
    
    for i in range(max_val):
        mayor_tiempo = 0
        for k in range(min(10, i)):  
            print(f"Iteracion {iter}/{total_iters}")
            ms_que_llevo = correrTest(i, k)
            if mayor_tiempo < ms_que_llevo:
                mayor_tiempo = ms_que_llevo
            iter += 1
        tiempos.append(mayor_tiempo)
    
    plt.figure(figsize=(10, 7))
    
    plt.plot(cantidad_maestros, tiempos, 'o', color='red')
    
    plt.xlabel('Número de maestros (n)')
    plt.xticks([i for i in range(max_val)])
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.title('Tiempos de ejecución para diferentes valores de n y k')
    plt.savefig('images/graficoBacktracking2.png', format="png")
    plt.show()

        
def correrTest(n, k):
    maestros_y_habilidades = generar_test(n)
    inicio = time.time()
    # A priori solo nos interesa el tiempo en esta seccion 
    problema_tribu_del_agua_bt(maestros_y_habilidades, k)
    fin = time.time()

    msQueLlevo = int((fin - inicio) * 1000)

    return msQueLlevo

generar_tests_y_graficar()