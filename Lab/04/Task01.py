# Task 1
from queue import PriorityQueue

def heuristic(current_pos, end_pos):
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  
        self.f = 0  

    def __lt__(self, other):
        return self.f < other.f

def best_first_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    
    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()
    
    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position
        
        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        visited.add(current_pos)
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                    maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited):
                new_node = Node(new_pos, current_node)
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h
                frontier.put(new_node)
                visited.add(new_pos)
    return None

def find_all_pairs_shortest_paths(maze, points):
    paths = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            path = best_first_search(maze, points[i], points[j])
            if path:
                paths[(points[i], points[j])] = path
                paths[(points[j], points[i])] = path[::-1]
    return paths

def greedy_tsp(maze, start, goals):
    all_points = [start] + goals
    paths = find_all_pairs_shortest_paths(maze, all_points)
    
    current = start
    visited = set()
    ordered_path = []
    
    while len(visited) < len(goals):
        visited.add(current)
        ordered_path.append(current)

        # Get the next closest goal with a valid path
        next_goal = min(
            (goal for goal in goals if goal not in visited and (current, goal) in paths),
            key=lambda x: len(paths[(current, x)]),
            default=None
        )

        if next_goal is None:  # No reachable goal left
            break

        ordered_path.extend(paths[(current, next_goal)][1:])  # Avoid duplicate points
        current = next_goal
    
    return ordered_path if len(visited) == len(goals) else None


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goals = [(4, 4), (1, 1), (0, 4), (4, 3)]

path = greedy_tsp(maze, start, goals)
if path:
    print("Path covering all goals:", path)
else:
    print("No path found")
