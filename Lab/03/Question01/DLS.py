class GoalBasedAgent:
    def __init__(self, target):
        self.target = target

    def perceive_goal(self, perception):
        if perception == self.target:
            return "Goal Achieved"
        else:
            return "Searching for Goal"

    def act(self, perception, environment, depth_limit):
        result = self.perceive_goal(perception)
        if result == "Goal Achieved":
            print("Already at the Goal")
        else:
            return environment.depth_limited_search(perception, self.target, depth_limit)


class Environment:
    def __init__(self, structure):
        self.structure = structure

    def depth_limited_search(self, start, target, depth_limit):
        visited = []

        def dfs(node, target, depth):
            visited.append(node)
            if depth > depth_limit:
                return False
            if node == target:
                print(f"Path: {visited}")
                return True
            for neighbor in self.structure.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, target, depth + 1):
                        return True
            visited.pop()
            return False

        return dfs(start, target, 0)


def run_agent(agent, environment, starting_node, depth_limit):
    if not agent.act(starting_node, environment, depth_limit):
        print("Goal not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

starting_node = 'A'
goal_node = 'I'
depth_limit = 3

agent = GoalBasedAgent(goal_node)
environment = Environment(graph)
run_agent(agent, environment, starting_node, depth_limit)
