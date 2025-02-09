class UtilityBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def perceive_goal(self, percept):
        return "Goal Reached" if percept == self.goal else "Searching For Goal"

    def act(self, percept, environment):
        if self.perceive_goal(percept) == "Goal Reached":
            print("Already at Goal")
        else:
            result = environment.uniform_cost_search(percept, self.goal)
            if result is None:
                print("No Path Found")


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def uniform_cost_search(self, start, goal):
        frontier = [(start, 0)]
        visited = set()
        cost_so_far = {start: 0}
        came_from = {start: None}

        while frontier:
            frontier.sort(key=lambda x: x[1])
            cur_node, cur_cost = frontier.pop(0)

            if cur_node in visited:
                continue
            visited.add(cur_node)

            if cur_node == goal:
                path = []
                while cur_node is not None:
                    path.append(cur_node)
                    cur_node = came_from[cur_node]
                path.reverse()
                print(f"Path: {path}, Cost: {cur_cost}")
                return path

            for neighbor, cost in self.graph.get(cur_node, {}).items():
                new_cost = cur_cost + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = cur_node
                    frontier.append((neighbor, new_cost))

        return None


def run_agent(agent, environment, start_node):
    agent.act(start_node, environment)


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

start_node = 'A'
goal_node = 'I'

agent = UtilityBasedAgent(goal_node)
environment = Environment(graph)
run_agent(agent, environment, start_node)
