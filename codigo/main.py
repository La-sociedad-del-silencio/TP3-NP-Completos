from sys import argv
from backtracking_con_greedy import problema_tribu_del_agua_bt_greedy

from archivos import procesar_archivo
from pruebas import *
CIAN = '\033[96m'
FINCO = '\033[0m'

titulos = {
    FLAGBTGREEDY: "BACKTRACKING",
    FLAGPL : "PROGRAMACIÓN LINEAL",
    FLAGAPROXCATEDRA : "APROXIMACIÓN DE LA CÁTEDRA",
    FLAGAPROXADICIONAL : "APROXIMACIÓN ADICIONAL",
}

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
            ejecutar_tests_con_algoritmo("BACKTRACKING", problema_tribu_del_agua_bt_greedy, maxima_cantidad_de_tests)
            
def ejecutar_tests_con_algoritmo(titulo, algoritmo, maxima_cantidad_de_tests):
        print(CIAN + f"\n----{titulo}----\n\n" + FINCO)
        
        print("---Ejemplos adicionales---\n")
        generarResultados("ejemplos_adicionales", algoritmo, None)
        
        print("---Ejemplos mediciones---\n")
        generarResultados("ejemplos_mediciones", algoritmo, 53) 
    
        print("---Ejemplos de la cátedra---\n")
        generarResultados("ejemplos_catedra", algoritmo, maxima_cantidad_de_tests)
        
        #print("---Faltan correr---\n")
        #generarResultados("faltan_correr_greedy", algoritmo, None)

def procesar_algoritmo_a_utilizar(argv, posicion, maxima_cantidad_de_tests):
    problema_tribu_del_agua = problema_tribu_del_agua_bt_greedy # por defecto
    titulo = "BACKTRACKING"
    if argv[posicion] in algoritmos:
        problema_tribu_del_agua = algoritmos[argv[posicion]]
        titulo = titulos[argv[posicion]]
    ejecutar_tests_con_algoritmo(titulo, problema_tribu_del_agua, maxima_cantidad_de_tests)
        
            

main()