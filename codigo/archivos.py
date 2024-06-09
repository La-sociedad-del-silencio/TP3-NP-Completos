import time
from backtracking import problema_tribu_del_agua_bt
from backtracking_con_greedy import problema_tribu_del_agua_bt_greedy
from programacion_lineal import problema_tribu_del_agua_pl

CIAN = '\033[96m'
FINCO = '\033[0m'

FLAGBACKTRACKING = "--bt"
FLAGBTGREEDY = "--btg"
FLAGPL = "--pl"
FLAGAPROXCATEDRA = "--a1"
FLAGAPROXADICIONAL = "--a2"


algoritmos = {
    FLAGBACKTRACKING : problema_tribu_del_agua_bt,
    FLAGBTGREEDY : problema_tribu_del_agua_bt_greedy,
    FLAGPL : problema_tribu_del_agua_pl
}

titulos = {
    FLAGBACKTRACKING: "BACKTRACKING",
    FLAGBTGREEDY: "BACKTRACKING MEJORADO",
    FLAGPL : "PROGRAMACIÓN LINEAL",
    FLAGAPROXCATEDRA : "APROXIMACIÓN DE LA CÁTEDRA",
    FLAGAPROXADICIONAL : "APROXIMACIÓN ADICIONAL",
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
        ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, algoritmos[argv[2]], titulos[argv[2]])  
    
    else:
        ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, problema_tribu_del_agua_bt_greedy, titulos[FLAGBTGREEDY])
        ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, problema_tribu_del_agua_pl, titulos[FLAGPL])
        # Aprox 1
        # Aprox 2  
        
        
def ejecutar_algoritmo_e_imprimir_resultado(maestros_y_habilidades, k, algoritmo, titulo):
    inicio = time.time()

    grupos, coeficiente = algoritmo(maestros_y_habilidades, k)

    fin = time.time()

    tiempoQueLlevo = int((fin - inicio) * 1000)
    print(CIAN + f"\n----{titulo}----\n" + FINCO)
    
    for i, grupo in enumerate(grupos):
        print(f"Grupo {i+1}: {grupo}")
    print(f'Coeficiente: {coeficiente}')
    print(f"Tiempo total: {tiempoQueLlevo} mili-segundos") 
    