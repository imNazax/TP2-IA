import heapq

def b_heuristica(posicion_inicial, objetivo):
    cola = []
    # Iniciar la cola con la posición inicial y una prioridad calculada
    heapq.heappush(cola, (0, posicion_inicial))
    
    visitados = set()  # Para evitar revisitar los estados

    while cola:
        prioridad_actual, posicion_actual = heapq.heappop(cola)
        if posicion_actual in visitados:
            continue
        visitados.add(posicion_actual)
        
        # Función de prueba para determinar si es la posición objetivo
        if posicion_actual == objetivo:
            return posicion_actual
        
        # Generar posibles movimientos (simulando pequeños desplazamientos)
        for desplazamiento in [-1, 1]:  # Simulación de movimientos a izquierda y derecha
            nueva_posicion = posicion_actual + desplazamiento
            if nueva_posicion not in visitados:
                # Calcular nueva prioridad basada en la distancia al objetivo
                nueva_prioridad = abs(objetivo - nueva_posicion)
                heapq.heappush(cola, (nueva_prioridad, nueva_posicion))
    
    return None  # Si no se encuentra la posición adecuada

# Uso del algoritmo
posicion_inicial = 0
objetivo = 10  # Supongamos que la posición objetivo es 10
resultado = b_heuristica(posicion_inicial, objetivo)
print("Posicion encontrada:", resultado if resultado is not None else "No encontrada")