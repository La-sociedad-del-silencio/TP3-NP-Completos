from sys import argv
from backtracking_con_greedy import problema_tribu_del_agua_bt_greedy

from archivos import procesar_archivo
from pruebas import *

def main():
    
    if len(argv) > 1 and not argv[1].isdigit() and not argv[1].startswith("--"):
        procesar_archivo(argv) 
        
    else:
        # TESTS / EJEMPLOS
        
        maxima_cantidad_de_tests = None
        if len(argv) > 1 and argv[1].isdigit():
            maxima_cantidad_de_tests = int(argv[1])
            
        if len(argv) > 1 and argv[1].startswith("--"):
            procesar_algoritmo_a_utilizar(argv, 1, maxima_cantidad_de_tests)
                
        elif len(argv) > 2:
            procesar_algoritmo_a_utilizar(argv, 2, maxima_cantidad_de_tests)
            
        else:
            ejecutar_tests_con_algoritmo("BACKTRACKING", problema_tribu_del_agua_bt_greedy, maxima_cantidad_de_tests, False)
            
def ejecutar_tests_con_algoritmo(titulo, algoritmo, maxima_cantidad_de_tests, calcular_cota):
        print(CIAN + f"\n----{titulo}----\n\n" + FINCO)
        
        print("---Ejemplos adicionales---\n")
        _, cota1 = generarResultados("ejemplos_adicionales", algoritmo, None, calcular_cota)
        
        print("---Ejemplos mediciones---\n")
        _, cota2 = generarResultados("ejemplos_mediciones", algoritmo, None, calcular_cota) 
    
        print("---Ejemplos de la cátedra---\n")
        _, cota3 = generarResultados("ejemplos_catedra", algoritmo, maxima_cantidad_de_tests, calcular_cota) 
                
        if calcular_cota:
            cota = max(cota1, cota2, cota3)
            print(f"Cota de aproximación empírica para todos los sets de datos: {cota}\n")
            
def procesar_algoritmo_a_utilizar(argv, posicion, maxima_cantidad_de_tests):
    problema_tribu_del_agua = problema_tribu_del_agua_bt_greedy # por defecto
    titulo = "BACKTRACKING"
    if argv[posicion] in algoritmos:
        problema_tribu_del_agua = algoritmos[argv[posicion]]
        titulo = titulos[argv[posicion]]
    casos_con_cota = {titulos[FLAGPL], titulos[FLAGAPROXCATEDRA], titulos[FLAGAPROXADICIONAL]}
    calcular_cota = False
    if titulo in casos_con_cota:
        calcular_cota = True
    ejecutar_tests_con_algoritmo(titulo, problema_tribu_del_agua, maxima_cantidad_de_tests, calcular_cota)
        
            

main()
