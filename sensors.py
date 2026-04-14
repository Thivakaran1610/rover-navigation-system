import random

def get_ultrasonic_distance():
    return random.randint(5, 100)

def get_ir_status():
    # 0 = clear, 1 = obstacle
    return random.choice([0, 1])

def read_all_sensors():
    return {
        "distance": get_ultrasonic_distance(),
        "ir": get_ir_status()
    }
