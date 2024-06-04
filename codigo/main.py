from sys import argv
import time

from archivos import procesar_archivo
from pruebas import *
CIAN = '\033[96m'
FINCO = '\033[0m'

FLAGMOSTRARSECUENCIA = "--mostrarSecuencia"

def main():
    f'''
    INPUT (argv):
        - argv[1] = Nombre del archvio a procesar o cantidad máxima de tests de la cátedar a ejecutar
    OUTPUT (stdout):
        - Grupos S_i
        - El tiempo que llevó calcular todo
    '''
    
    if len(argv) > 1 and not argv[1].isdigit():
        procesar_archivo(argv) 
        
    else:
        # TESTS / EJEMPLOS
        
        print(CIAN + "\n----BACKTRACKING----\n\n" + FINCO)
        
        maxima_cantidad_de_tests = None
        if len(argv) > 1:
            maxima_cantidad_de_tests = int(argv[1])
        
        print("---Ejemplos adicionales---\n")
        generarResultados("ejemplos_adicionales", None)
        
        print("---Ejemplos mediciones---\n")
        generarResultados("ejemplos_mediciones", 54) # hasta 10_9, sin contar k=0
    
        print("---Ejemplos de la cátedra---\n")
        generarResultados("ejemplos_catedra", maxima_cantidad_de_tests)
            

main()