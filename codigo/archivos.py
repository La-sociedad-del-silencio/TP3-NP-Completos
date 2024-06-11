import time
from backtracking_con_greedy import problema_tribu_del_agua_bt_greedy

FLAGBTGREEDY = "--btg"
FLAGPL = "--pl"
FLAGAPROXCATEDRA = "--a1"
FLAGAPROXADICIONAL = "--a2"

algoritmos = {
    FLAGBTGREEDY : problema_tribu_del_agua_bt_greedy,
}

def generarTestDe(archivo):
    k = None
    maestros_y_habilidades = []

    with open(archivo, "r") as file:
        for i, line in enumerate(file):
            line = line.strip()
            if line.startswith("#"):
                continue
            if k is None:
                k = int(line)
                continue
            maestro, habilidad = line.split(", ")
            maestros_y_habilidades.append((maestro, int(habilidad)))

    return maestros_y_habilidades, k

def procesar_archivo(argv):
    """ 
    Dado el primer argumento pasado por línea de comandos, procesa los datos
    del archivo correspondiente y calcula .... Si se usa el flag... . Caso contrario, 
    ...
    """

    archivoAProcesar = argv[1]
    
    maestros_y_habilidades, k = generarTestDe(archivoAProcesar)
        
    if len(argv) > 2 and argv[2] in algoritmos:
        ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, algoritmos[argv[2]])  
    
    else:
        ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, problema_tribu_del_agua_bt_greedy)
        # PL
        # Aprox 1
        # Aprox 2  
        
        
def ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, algoritmo):
    inicio = time.time()

    grupos, coeficiente = algoritmo(maestros_y_habilidades, k)

    fin = time.time()

    tiempoQueLlevo = int((fin - inicio) * 1000)
      
    for i, grupo in enumerate(grupos):
        print(f"Grupo {i+1}: {grupo}")
    print(f'Coeficiente: {coeficiente}')
    print(f"Tiempo total: {tiempoQueLlevo} mili-segundos") 
    