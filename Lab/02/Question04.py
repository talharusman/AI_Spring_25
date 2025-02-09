import random

class Environment:
    def __init__(self):
        self.vulnerabilities = {chr(i): random.choice(["Safe", "Low Risk Vulnerable", "High Risk Vulnerable"]) for i in range(ord('A'), ord('I') + 1)}

    def display(self):
        print("System State:")
        for component, state in self.vulnerabilities.items():
            print(f"Component {component}: {state}")
        print()

    def get_vulnerabilities(self):
        return self.vulnerabilities

    def get_vulnerability(self, component):
        return self.vulnerabilities.get(component, None)

    def set_vulnerability(self, component, state):
        if component in self.vulnerabilities:
            self.vulnerabilities[component] = state


class SecurityAgent:
    def __init__(self):
        self.patching = []

    def scan(self, env):
        print("Starting System Scan...")
        for component, state in env.get_vulnerabilities().items():
            if state == "Safe":
                print(f"Component {component} is Safe. Logging success.")
            else:
                print(f"Component {component} has vulnerabilities. Logging warning.")
                self.patching.append(component)

    def patch_vulnerabilities(self, env):
        print("\nPatching Vulnerabilities...")
        for component in self.patching:
            state = env.get_vulnerability(component)
            if state == "Low Risk Vulnerable":
                env.set_vulnerability(component, "Safe")
                print(f"Patched Low Risk Vulnerability in Component {component}.")
            elif state == "High Risk Vulnerable":
                print(f"Component {component} requires premium service to patch High Risk Vulnerabilities.")


def run_agent(agent, env):
    print("Initial System State:")
    env.display()
    agent.scan(env)
    agent.patch_vulnerabilities(env)
    print("\nFinal System State:")
    env.display()


env = Environment()
agent = SecurityAgent()
run_agent(agent, env)