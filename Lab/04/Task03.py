import heapq

# Graph with edge costs (travel times)
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

# Time windows for each node (earliest time, latest time)
time_windows = {
    'A': (0, 12), 
    'B': (1, 10),   
    'C': (1, 9),   
    'D': (4, 12),
    'E': (5, 14),  
    'F': (2, 10),   
    'G': (3, 13),  
    'H': (7, 16),
    'I': (9, 18)   
}

def greedy_bfs_with_time(graph, start, goal, heuristic, time_windows):
    pq = []  
    heapq.heappush(pq, (heuristic[start], start, 0))  # (heuristic, node, arrival_time)
    
    best_time = {node: float('inf') for node in graph}  
    best_time[start] = 0
    
    came_from = {start: None}

    while pq:
        _, current_node, current_time = heapq.heappop(pq)

        # If reached goal within its time window, reconstruct path
        if current_node == goal:
            if time_windows[goal][0] <= current_time <= time_windows[goal][1]:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"Goal reached. Optimal path: {path}")
                return
            else:
                continue  # Goal reached outside time window, ignore this path

        print(f"Visiting {current_node} at time {current_time}")

        for neighbor, travel_time in graph[current_node].items():
            arrival_time = current_time + travel_time

            # Adjust arrival time to fit within time window
            if arrival_time < time_windows[neighbor][0]:
                arrival_time = time_windows[neighbor][0]  # Wait until allowed

            # If arrival time is within time window and better than previous, update
            if time_windows[neighbor][0] <= arrival_time <= time_windows[neighbor][1] and arrival_time < best_time[neighbor]:
                best_time[neighbor] = arrival_time
                came_from[neighbor] = current_node
                heapq.heappush(pq, (heuristic[neighbor], neighbor, arrival_time))

    print("Goal not reachable within time constraints.")

print("\nOptimized Delivery Route with Time Constraints:")
greedy_bfs_with_time(graph, 'A', 'I', heuristic, time_windows)
