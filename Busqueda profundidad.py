############################################################################################
# Se define una función busqueda_en_profundidad. El objetivo es mover el bloque desde una  #
# posición inicial, representada por el valor B, hasta una posición deseada, representada  #
# por el valor A.                                                                          #
# El algoritmo realiza una búsqueda exhaustiva en cada rama antes de retroceder. Comienza  #
# verificando si la posición actual (B) es igual a la posición deseada (A). Si es así, se  #
# devuelve una lista con los movimientos realizados hasta ese punto, lo que indica que se  #
# ha encontrado una solución.                                                              #
# En caso contrario, se generan los movimientos posibles desde la posición actual          #
# (B-1 y B+1). A continuación, se realiza una llamada recursiva a la función para cada     # 
# movimiento posible. El objetivo es explorar todas las ramas del árbol de búsqueda.       #
# Si se encuentra una solución en alguna de las ramas exploradas, se devuelve una lista de #
# movimientos que incluye la posición actual (B) y los movimientos realizados hasta ese    #
# punto. Si no se encuentra solución en ninguna de las ramas exploradas, se retorna None   #
# para indicar que no se ha encontrado una solución.                                       #
############################################################################################

def busqueda_en_profundidad(B, A):
    # Se verifica si se ha alcanzado el valor deseado
    if B == A:
        return [B]  # Se devolve la lista de movimientos realizados

    # Se generan los movimientos posibles
    movimientos_posibles = [B-1, B+1]

    # Se recorren los movimientos posibles
    for movimiento in movimientos_posibles:
        # Se realiza el movimiento
        movimientos = busqueda_en_profundidad(movimiento, A)
        if movimientos is not None:
            return [B] + movimientos

    # Si no se encuentra solución, se retorna None
    return None

# Damos valores para ejemplificar, imaginamos que B se encuentra a 10cm de A.
valor_inicial_B = 10
valor_objetivo_A = 0

# Realizamos la Llamada a la función de búsqueda en profundidad y pasamos como
# parámetro los valores iniciales definidos anteriormente
resultado = busqueda_en_profundidad(valor_inicial_B, valor_objetivo_A)

if resultado:
    print("Se ha logrado ubicar el bloque en la posición deseada.")
    print(f"Los movimientos realizados fueron: {resultado}")
else:
    print("No se ha encontrado una solución.")
