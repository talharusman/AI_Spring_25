class GoalBasedAgent:
    def __init__(self, target):
        self.target = target

    def perceive_goal(self, perception):
        if perception == self.target:
            return "Goal Achieved"
        else:
            return "Searching for Goal"

    def act(self, perception, environment):
        result = self.perceive_goal(perception)
        if result == "Goal Achieved":
            print("Already at the Goal")
        else:
            environment.depth_first_search(perception, self.target)


class Environment:
    def __init__(self, structure):
        self.structure = structure

    def depth_first_search(self, start, target):
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            current_node = stack.pop()
            print(f"Visiting Node: {current_node}")
            if current_node == target:
                print("Goal Achieved!!!!\n")
                return
            for neighbor in reversed(self.structure.get(current_node, [])):
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        print("Goal Not Found")


def run_agent(agent, environment, starting_node):
    agent.act(starting_node, environment)


tree_structure = {
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

agent = GoalBasedAgent(goal_node)
environment = Environment(tree_structure)
run_agent(agent, environment, starting_node)
