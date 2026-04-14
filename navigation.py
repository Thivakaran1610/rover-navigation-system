from config import SAFE_DISTANCE
from motor_control import move_forward, stop, turn_left, turn_right

def obstacle_avoidance(sensor_data):
    distance = sensor_data["distance"]
    ir = sensor_data["ir"]

    if distance < SAFE_DISTANCE or ir == 1:
        stop()
        decision = choose_direction()
        return decision
    else:
        move_forward(60)
        return "Moving Forward"

def choose_direction():
    import random

    direction = random.choice(["left", "right"])

    if direction == "left":
        turn_left()
    else:
        turn_right()

    return f"Obstacle detected - turning {direction}"
