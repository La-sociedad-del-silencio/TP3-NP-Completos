from sys import argv
import time

from archivos import procesar_archivo
from pruebas import *

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
        
        maxima_cantidad_de_tests = None
        if len(argv) > 1:
            maxima_cantidad_de_tests = int(argv[1])
        
        print("---Ejemplos adicionales---\n")
        generarResultados("ejemplos_adicionales", None)
    
        print("---Ejemplos de la cátedra---\n")
        generarResultados("ejemplos_catedra", maxima_cantidad_de_tests)
            

main()