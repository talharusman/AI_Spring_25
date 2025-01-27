import random

class Enviourment:
    def __init__(self) -> None:
        self.components = {chr(i): random.choice(["vulnerable", "safe"]) for i in range(ord('A'), ord('I') + 1)}
    
    def Display_state(self):
        print(self.components)

    def get_components(self):
        return self.components
    
    def Set_Component(self, State, component):
        self.components[component] = State


class SecurityAgent:
    def __init__(self, environment) -> None:
        self.environment = environment
        self.components = environment.get_components()

    def System_Scan(self):
        vulnerable_components = []
        for key, value in self.environment.components.items():
            if value == "vulnerable":
                vulnerable_components.append(key)
                print(f"Warning: Component {key} is vulnerable.")
            else:
                print(f"Success: Component {key} is secure.")
        return vulnerable_components

    def Patching_Vulnerabilities(self):
        for key, value in self.environment.components.items():
            if value == "vulnerable":
                self.environment.Set_Component("safe", key)
                print(f"Component {key} has been patched.")
            else:
                print(f"Component {key} is already secure.")

    def Display(self):
        for key, value in self.environment.components.items():
            print(f"{key}: {value}")


enviourment = Enviourment()
agent = SecurityAgent(enviourment)
agent.System_Scan()
agent.Patching_Vulnerabilities()
agent.Display()