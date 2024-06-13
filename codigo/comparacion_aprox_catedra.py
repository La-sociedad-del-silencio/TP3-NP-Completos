from backtracking_con_greedy import problema_tribu_del_agua_bt_greedy
from aproximacion_catedra import problema_tribu_del_agua_aprox_catedra
from pruebas import generarResultados
import numpy as np
import matplotlib.pyplot as plt

from random import randint

# grupos, cota1 = generarResultados("ejemplos_catedra", problema_tribu_del_agua_aprox_catedra, None, True)

def generar_test(cantidad):
    maestros_y_habilidades = []
    k = randint(1, cantidad) 
    
    for i in range(cantidad):
        habilidad = randint(500, 1000)
        nombre = f'Maestro {i}: '
        # nombre += str(hex(hash(nombre)))
        maestros_y_habilidades.append((nombre, habilidad))
        
    return maestros_y_habilidades, k 


def comparar(cantidad):
    maestros_y_habilidades, k = generar_test(cantidad)
    print("Corro real")
    _, coeficienteReal =  problema_tribu_del_agua_bt_greedy(maestros_y_habilidades, k)
    print("Corro aprox")
    _, coeficienteAprox =  problema_tribu_del_agua_aprox_catedra(maestros_y_habilidades, k)
    print(coeficienteReal)
    print(coeficienteAprox)

    return coeficienteAprox/coeficienteReal

def obtenerMediciones(maxCant):
    coeficientes = []
    cantidadDeMaestros = []
    for i in range(1, maxCant):
        print(f"Test: {i}")
        cantidadDeMaestros.append(i)
        coeficientes.append(comparar(i))

    return cantidadDeMaestros, coeficientes

def graficar(maxCant):
    cantidadDeMaestros, coeficientes = obtenerMediciones(maxCant)
    plt.plot(cantidadDeMaestros, coeficientes, 'bo')
    plt.savefig(f'images/coeficientesAprox.png', format="png")
    plt.show()

#Cambiar este numero si queres mas
#graficar(15)
