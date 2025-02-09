class Environment:
    def __init__(self):
        self.grid = {
            "a": " ", "b": " ", "c": "🔥",
            "d": " ", "e": "🔥", "f": " ",
            "g": " ", "h": " ", "j": "🔥"
        }

    def display(self):
        print("Environment Status:")
        print(f"{self.grid['a']} {self.grid['b']} {self.grid['c']}")
        print(f"{self.grid['d']} {self.grid['e']} {self.grid['f']}")
        print(f"{self.grid['g']} {self.grid['h']} {self.grid['j']}")
        print()

    def get_room_status(self, room):
        return self.grid[room]

    def extinguish_fire(self, room):
        self.grid[room] = " "


class FirefightingRobot:
    def __init__(self):
        self.current_location = "a"

    def move_to(self, room):
        print(f"Moving to room {room}...")
        self.current_location = room

    def check_and_extinguish_fire(self, env):
        status = env.get_room_status(self.current_location)
        if status == "🔥":
            print(f"Fire detected in room {self.current_location}! Extinguishing fire...")
            env.extinguish_fire(self.current_location)
        else:
            print(f"Room {self.current_location} is safe.")


def run_robot(robot, env):
    path = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]
    print("Initial Environment Status:")
    env.display()

    for room in path:
        robot.move_to(room)
        robot.check_and_extinguish_fire(env)
        env.display()

    print("All rooms have been checked, and fires extinguished.")


env = Environment()
robot = FirefightingRobot()
run_robot(robot, env)
