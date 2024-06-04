from backtracking import problema_tribu_del_agua_bt
from archivos import *
import time

VERDE = '\033[92m'
ROJO  = '\033[91m'
FINCO = '\033[0m'

class Resultado:
    def __init__(self, obtenido, esperado, nombre_test, tiempo, habilidad_por_maestro):
        self.obtenido = obtenido

        self.esperado = esperado
        
        self.nombre_test = nombre_test            
        
        self.tiempo = tiempo
        
        self.datos = habilidad_por_maestro

    def __repr__(self) -> str:

        representacion = f"Test '{self.nombre_test}'" 
            
        representacion += "\n\n"
        representacion += "Tiempo total: " + str(self.tiempo) + " milisegundos"
        representacion += "\n\n"
        representacion += "Grupos:\n" 
        representacion += "\tResultado esperado: " + str(self.esperado[0])
        representacion += "\n"
        representacion += "\tResultado obtenido: " + str(self.obtenido[0])
        representacion += "\n\n"
        representacion += "Coeficiente:\n" 
        representacion += "\tResultado esperado: " + str(self.esperado[1])
        representacion += "\n"
        representacion += "\tResultado obtenido: " + str(self.obtenido[1])
        representacion += "\n\n"
        
        if son_resultados_iguales(self.esperado, self.obtenido, self.datos):
            representacion += VERDE + "Resultado: :)" + FINCO
        else:
            representacion += ROJO + "Resultado: X" + FINCO
        representacion += "\n"

        return representacion
    
def son_resultados_iguales(resultado_esperado, resultado_obtenido, habilidad_por_maestro):
    if resultado_esperado[1] == resultado_obtenido[1]:
        return False
    
    # Puede haber más de una combinación que de el mismo coeficiente
    suma = 0
    for grupo in resultado_obtenido[0]:
        suma_grupo = 0
        for maestro in grupo:
            suma_grupo += habilidad_por_maestro[maestro]
        suma += suma_grupo ** 2
    return suma == resultado_obtenido[1]

def generarRtasEsperadas(archivo):
    """ 
    Crea un diccionario con las respuestas esperadas para los ejemplos
    que figuran en el archivo. 
    """
    rtas = {}
    
    with open(archivo, "r") as f:
    
        nombre_archivo = None
        grupos  = []
        coeficiente = None
        
        for linea in f:
            linea = linea.strip()
            
            if linea.endswith('.txt'):
                nombre_archivo = linea
            elif linea.startswith('Grupo'):
                grupo = linea.split(': ')[1]
                maestros = grupo.split(", ")
                grupos.append(set(maestros))
            elif linea.startswith('Coeficiente: '):
                coeficiente = linea.split(': ')[1]
                rtas[nombre_archivo] = (grupos, coeficiente)
                grupos = []
            
        #rtas[nombre_archivo] = (cantidad_tropas, [estrategias])

    return rtas 

def generarResultados(carpeta, problema_tribu_del_agua, maximo):
    """ 
    Dado un directorio con ejemplos y las respuestas esperadas, ejecuta
    el programa en cada uno de ellos y devuelve una lista con los resultados
    obtenidos.
    """
    archivo_rtas_esperadas = f"{carpeta}/Resultados_Esperados.txt"
    rtas = generarRtasEsperadas(archivo_rtas_esperadas)
    cantidad_tests = 0
    for archivo, rtaEsperada in rtas.items():
        if maximo is not None and cantidad_tests == maximo:
            break
        
        maestros_y_habilidades, k = generarTestDe(carpeta + "/" + archivo)
        if k == 0: continue
        
        dic_habilidades = {}
        for maestro, habilidad in maestros_y_habilidades:
            dic_habilidades[maestro] = habilidad
        
        inicio = time.time()
        rta_obtenida = problema_tribu_del_agua(maestros_y_habilidades, k)
        fin = time.time()
        tiempoQueLlevo = int((fin - inicio) * 1000)
        resultado = Resultado(rta_obtenida, rtaEsperada, archivo, tiempoQueLlevo, dic_habilidades)

        print(resultado)
        cantidad_tests += 1
