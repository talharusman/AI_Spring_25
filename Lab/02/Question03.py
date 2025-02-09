import random

class Environment:
    def __init__(self):
        self.backup_tasks = [
            {"Task": f"Backup {i+1}", "Status": random.choice(["Failed", "Completed"])}
            for i in range(10)
        ]

    def get_task_status(self, task_index):
        return self.backup_tasks[task_index]["Status"]

    def retry_task(self, task_index):
        if self.get_task_status(task_index) == "Failed":
            self.backup_tasks[task_index]["Status"] = "Completed"
            print(f"Retried and completed {self.backup_tasks[task_index]['Task']}.")
        else:
            print(f"{self.backup_tasks[task_index]['Task']} is already completed.")

    def display_tasks(self):
        print("\nBackup Task Statuses:")
        for i, task in enumerate(self.backup_tasks):
            print(f"{i+1}. {task['Task']} - {task['Status']}")


class BackupManagementAgent:
    def __init__(self):
        self.current_task_index = 0

    def act(self, task_status):
        if task_status == "Failed":
            return "Retrying failed task"
        elif task_status == "Completed":
            return "Task is already completed"

    def move_to_next_task(self):
        self.current_task_index += 1


def run_backup_management_agent(agent, environment):
    for _ in range(len(environment.backup_tasks)):
        task_index = agent.current_task_index
        task_status = environment.get_task_status(task_index)
        print(f"Checking {environment.backup_tasks[task_index]['Task']}: {task_status}")

        if task_status == "Failed":
            print(agent.act(task_status))
            environment.retry_task(task_index)
        else:
            print(agent.act(task_status))

        agent.move_to_next_task()


environment = Environment()
agent = BackupManagementAgent()

print("Initial Task Statuses:")
environment.display_tasks()

run_backup_management_agent(agent, environment)

print("\nUpdated Task Statuses:")
environment.display_tasks()
