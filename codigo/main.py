from sys import argv
from backtracking_con_greedy import problema_tribu_del_agua_bt_greedy

from archivos import procesar_archivo
from pruebas import *

def main():
    f'''
    INPUT (argv):
        - argv[1] = Nombre del archvio a procesar o cantidad máxima de tests de la cátedar a ejecutar
        - argv[2] = Algoritmo a utilizar
            --b: backtracking
            
    OUTPUT (stdout):
        - Grupos S_i
        - El tiempo que llevó calcular todo
        - argv[1] y argv[2] son opcionales
        - Si argv[1] es el nombre de un archivo, se ejecuta solo ese. Caso contrario, se ejecutan todos
        - Si argv[1] es un número, indica la cantidad máxima de tests de la cátedra a ejecutar
        - Si argv[2] existe, es un flag e indica el algoritmo a utilizar
        - Si argv[2] no existe y no se quiere limitar los tests de la cátedra, argv[1] puede ser el flag
    '''
    
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
        _, cota2 = generarResultados("ejemplos_mediciones", algoritmo, 53, calcular_cota) 
    
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
    casos_con_cota = {titulos[FLAGPL], titulos[FLAGAPROXCATEDRA]}
    calcular_cota = False
    if titulo in casos_con_cota:
        calcular_cota = True
    ejecutar_tests_con_algoritmo(titulo, problema_tribu_del_agua, maxima_cantidad_de_tests, calcular_cota)
        
            

main()