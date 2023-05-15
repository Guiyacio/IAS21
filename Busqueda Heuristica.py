##########################################################################################
# Se define la función busqueda_heuristica que tiene como objetivo mover el bloque desde #
# una posición inicial, representada por el valor valor_inicial_b, hasta una posición    #
# deseada, representada por el valor valor_objetivo_a.                                   #
# El algoritmo se basa en la utilización de una heurística que calcula la distancia      #
# Euclidiana entre la posición actual y la posición deseada. Cuanto menor sea la         #
# distancia, más cercano estará el bloque a la posición deseada.                         #
# La función comienza inicializando el nodo actual con la posición inicial y calculando  #
# la distancia Euclidiana entre esta posición y la posición deseada.                     #
# A continuación, entra en un bucle en el que generará posibles movimientos hacia la     #
# izquierda y hacia la derecha. Para cada movimiento, actualiza la posición actual y     #
# calcula la nueva distancia Euclidiana.                                                 #
# El algoritmo selecciona el movimiento que reduzca la distancia Euclidiana de manera más#
# significativa en cada iteración.                                                       #
# El bucle se repite hasta que la posición actual sea igual a la posición deseada, lo que#
# significa que se ha ubicado correctamente el bloque.                                   #
##########################################################################################

import math

# Se Definen las coordenadas de la posición inicial y la posición deseada
posicion_actual = (10, 0)  # Coordenadas (x, y) de la posición inicial B
posicion_deseada = (0, 0)  # Coordenadas (x, y) de la posición deseada A

# Función para calcular la distancia Euclidiana entre dos puntos
def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

# Se calcula la distancia Euclidiana entre la posición actual y la posición deseada
distancia_actual = distancia_euclidiana(posicion_actual, posicion_deseada)

# Se generan movimientos hacia la izquierda y hacia la derecha y se evalua la distancia Euclidiana
movimientos = [-1, 1]  # Movimientos posibles: -1 para izquierda, 1 para derecha
mejor_movimiento = None
mejor_distancia = float('inf')  # Se inicializar con un valor infinito

for movimiento in movimientos:
    nueva_posicion = (posicion_actual[0] + movimiento, posicion_actual[1])
    distancia_nueva = distancia_euclidiana(nueva_posicion, posicion_deseada)
        
    if distancia_nueva < mejor_distancia:
        mejor_movimiento = movimiento
        mejor_distancia = distancia_nueva

# Se realiza el movimiento que reduzca la distancia Euclidiana de manera más significativa
posicion_actual = (posicion_actual[0] + mejor_movimiento, posicion_actual[1])

# Se repiten los pasos anteriores hasta que la distancia sea lo suficientemente pequeña
while mejor_distancia > 0.1:  # Por ejemplo, consideramos que una distancia menor a 0.1 es aceptable
    # Se calcula nuevamente la distancia Euclidiana y se busca el mejor movimiento
    print("Distancia Actual:", distancia_actual)
    distancia_actual = distancia_euclidiana(posicion_actual, posicion_deseada)
    for movimiento in movimientos:
        nueva_posicion = (posicion_actual[0] + movimiento, posicion_actual[1])
        distancia_nueva = distancia_euclidiana(nueva_posicion, posicion_deseada)
        
        if distancia_nueva < mejor_distancia:
            mejor_movimiento = movimiento
            mejor_distancia = distancia_nueva

    # Se Realiza el mejor movimiento encontrado
    posicion_actual = (posicion_actual[0] + mejor_movimiento, posicion_actual[1])

# Se imprimir la posición final del bloque
print("Posición final del bloque:", posicion_actual)
