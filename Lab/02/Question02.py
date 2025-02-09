class Environment:
    def __init__(self):
        self.servers = {
            "1": "Balanced",
            "2": "Underloaded",
            "3": "Overloaded",
            "4": "Balanced",
            "5": "Underloaded",
            "6": "Overloaded"
        }

    def get_server(self, position):
        return self.servers.get(position, "Not Found")

    def balance_server(self, position):
        if self.get_server(position) == "Overloaded":
            for server_id in self.servers:
                if self.servers[server_id] == "Underloaded":
                    self.servers[server_id] = "Balanced"
                    self.servers[position] = "Balanced"
                    print(f"Balanced server {position} by redistributing tasks to server {server_id}.")
                    return
            print(f"No underloaded server available to balance server {position}.")
        else:
            print(f"Server {position} is not overloaded.")
    
    def display(self):
        for server_id, status in self.servers.items():
            print(f"Server {server_id}: {status}")



class Agent:
    def __init__(self):
        self.server_position = "1"

    def act(self, prospect):
        if prospect == "Overloaded":
            return "Server is Balanced"
        elif prospect == "Underloaded":
            return "Server is Underloaded"
        else:
            return "Server is already Balanced"

    def move_server(self):
        self.server_position = str(int(self.server_position) + 1)


def run_agent(agent, environment):
    for _ in range(len(environment.servers)):
        position = agent.server_position
        prospect = environment.get_server(position)
        print(f"Checking server {position}: {prospect}")

        if prospect == "Overloaded":
            environment.balance_server(position)
            print(agent.act(prospect))
        else:
            print(agent.act(prospect))

        agent.move_server()



environment = Environment()
agent = Agent()

print("Initial Server States:")
for server_id, state in environment.servers.items():
    print(f"Server {server_id}: {state}")

run_agent(agent, environment)

print("\nUpdated Server States:")
environment.display()

