from queue import Queue, LifoQueue, PriorityQueue

# Se define el pequeño grafo de 6 posiciones
graph = {
    'B': ['C', 'E'],
    'C': ['D'],
    'D': ['A'],
    'E': ['F'],
    'F': ['A'],
    'A': []
}

# Heurística simulada: distancia "estimada" al objetivo
heuristic = {
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 1,
    'A': 0
}

# Búsqueda Primero en Anchura (Breadth-First Search)
def bfs(start, goal):
    visited = set()
    q = Queue()
    q.put((start, [start]))
    while not q.empty():
        node, path = q.get()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.put((neighbor, path + [neighbor]))

# Búsqueda Primero en Profundidad (Depth-First Search)
def dfs(start, goal):
    visited = set()
    stack = LifoQueue()
    stack.put((start, [start]))
    while not stack.empty():
        node, path = stack.get()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.put((neighbor, path + [neighbor]))

# Búsqueda Primero el Mejor (Greedy Best-First Search)
def greedy(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start, [start]))
    while not pq.empty():
        _, node, path = pq.get()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))

# Búsqueda A* (A-star Search)
def astar(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, start, [start]))  # (f = g + h, g, node, path)
    while not pq.empty():
        f, g, node, path = pq.get()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_g = g + 1  # supondremos que el costo entre nodos es 1
                new_f = new_g + heuristic[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

# Pruebas
start = 'B'
goal = 'A'

print("BFS:", bfs(start, goal))
print("DFS:", dfs(start, goal))
print("Greedy:", greedy(start, goal))
print("A*:", astar(start, goal))
