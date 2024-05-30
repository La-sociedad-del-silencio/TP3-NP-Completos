from sys import argv
import time

from archivos import procesar_archivo
from pruebas import *

FLAGMOSTRARSECUENCIA = "--mostrarSecuencia"

def main():
    f'''
    INPUT (argv):
        - argv[1] = Nombre del archvio a procesar
    OUTPUT (stdout):
        - Grupos S_i
        - El tiempo que llevó calcular todo
    '''
    
    if len(argv) > 1:
        procesar_archivo(argv) 
        
    else:
        # TESTS / EJEMPLOS
        
        print("---Ejemplos de la cátedra---\n")
        generarResultados("ejemplos_catedra")
            
        
        
        #print("---Ejemplos adicionales---\n")
        #for resultado in generarResultados("ejemplos_adicionales"):
        #    print(resultado)


main()