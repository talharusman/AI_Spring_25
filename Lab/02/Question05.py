import random

class Environment:
    def __init__(self):
        self.hospital_layout = {
            "corridors": ["Corridor 1", "Corridor 2", "Corridor 3"],
            "patient_rooms": {"Room 101": None, "Room 102": None, "Room 103": None},
            "nurse_stations": ["Nurse Station 1"],
            "medicine_storage": ["Storage 1"]
        }
        self.patient_schedules = {
            "Room 101": {"time": "9:00 AM", "medicine": "Medicine A"},
            "Room 102": {"time": "10:00 AM", "medicine": "Medicine B"},
            "Room 103": {"time": "11:00 AM", "medicine": "Medicine C"}
        }

    def display(self):
        print("Hospital Layout:")
        for key, value in self.hospital_layout.items():
            print(f"{key}: {value}")
        print()
        print("Patient Schedules:")
        for room, schedule in self.patient_schedules.items():
            print(f"{room}: {schedule}")

    def get_patient_schedule(self, room):
        return self.patient_schedules.get(room, None)


class HospitalRobot:
    def __init__(self):
        self.current_location = "Corridor 1"
        self.carrying_medicine = None

    def move_to(self, location):
        print(f"Moving to {location}...")
        self.current_location = location

    def pick_up_medicine(self, storage, medicine):
        print(f"Picking up {medicine} from {storage}...")
        self.carrying_medicine = medicine

    def deliver_medicine(self, room):
        print(f"Delivering {self.carrying_medicine} to {room}...")
        self.carrying_medicine = None

    def scan_patient_id(self, room):
        print(f"Scanning patient ID in {room}... Verification successful.")

    def alert_staff(self):
        print("Alerting staff for critical situations...")


def run_robot(robot, env):
    print("Initial Hospital State:")
    env.display()

    for room, schedule in env.patient_schedules.items():
        robot.move_to("Storage 1")
        robot.pick_up_medicine("Storage 1", schedule["medicine"])
        robot.move_to(room)
        robot.scan_patient_id(room)
        robot.deliver_medicine(room)

    print("\nAll tasks completed successfully.")


env = Environment()
robot = HospitalRobot()
run_robot(robot, env)
