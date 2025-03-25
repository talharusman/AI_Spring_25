# Task 2
import random
import time

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7,
    'F': 3, 'G': 6, 'H': 2, 'I': 0
}

def update_edge_costs(graph):
    for node in graph:
        for neighbor in graph[node]:
            graph[node][neighbor] = random.randint(1, 10)

def a_star(graph, start, goal):
    frontier = [(start, heuristic[start])]
    g_costs = {start: 0}
    came_from = {start: None}
    visited = set()
    
    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)
        
        if current_node in visited:
            continue

        visited.add(current_node)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return
        
        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost
            f_cost = new_g_cost + heuristic[neighbor]
            
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))
        
        # Simulate real-time changes in edge costs dynamically at randomintervals
        if random.random() < 0.3: 
            update_edge_costs(graph)
            print("\nEdge costs updated dynamically!")
            print(graph)  
            time.sleep(1)

print("\nFollowing is the A* Search:")
a_star(graph, 'A', 'I')
