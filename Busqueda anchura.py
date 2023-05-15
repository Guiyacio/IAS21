########################################################################################
# Definimos una función que realiza la búsqueda en anchura(breadth-first search, BFS)  #
# para encontrar una solución al problema planteado. El objetivo es mover el bloque    #
# desde una posición inicial, representada por valor_inicial_b, hasta una posición     #
# deseada, representada por el valor valor_objetivo_a.                                 #                                               #
########################################################################################

from collections import deque

def busqueda_anchura(B, A):
    # Se utiliza una cola para realizar la exploración de los nodos
    cola = deque()

    # Se comienza agregando el nodo inicial a la cola junto con una lista vacía que
    # representa el camino recorrido hasta el momento.
    
    #Se agrega el nodo inicial a la cola
    cola.append((B, []))  # (valor de B, lista de movimientos)

    # Se realiza un bucle donde se extrae el primer nodo de la cola y se verifica
    # si es el nodo deseado. Si lo es, se retorna el camino recorrido hasta ese punto.
    # Si el nodo extraído no es el deseado, se generan dos posibles movimientos:
    # uno hacia la izquierda y otro hacia la derecha. Estos movimientos se agregan a la
    # cola junto con el camino actualizado, que incluye el movimiento realizado.
    #
    # El bucle continúa extrayendo nodos de la cola y explorando sus movimientos
    # hasta encontrar el nodo deseado o hasta que la cola se quede vacía, lo que
    # indicaría que no se encontró una solución.
    
    while cola:
        # Se obtene el siguiente nodo de la cola
        nodo, movimientos = cola.popleft()

        # Se verificar si se ha alcanzado la posición de A
        if nodo == A:
            # Se ha encontrado la posición de A, se retornan los movimientos realizados
            return movimientos

        # Se generan los movimientos posibles
        movimientos_posibles = [nodo-1, nodo+1]

        # Se agregan los movimientos posibles a la cola
        for movimiento in movimientos_posibles:
            cola.append((movimiento, movimientos + [movimiento]))

    # Si no se encuentra la posición, retornar None
    return None

# Damos valores para ejemplificar, imaginamos que B se encuentra a 10cm de A.

valor_inicial_B = 10
valor_objetivo_A = 0

# Realizamos la Llamada a la función de búsqueda en anchura y pasamos como
# parámetro los valores iniciales definidos anteriormente

resultado = busqueda_anchura(valor_inicial_B, valor_objetivo_A)

if resultado:
    print("Se ha logrado ubicar el bloque en la posición deseada.")
    print(f"Los movimientos realizados fueron: {resultado}")
else:
    print("No se logró ubicar el bloque en la posición deseada.")
