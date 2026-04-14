from sensors import read_all_sensors
from navigation import obstacle_avoidance
from gps_module import get_location
import time

def main():
    print("Starting Autonomous Rover...\n")

    for _ in range(10):
        sensor_data = read_all_sensors()
        location = get_location()

        print("Sensor Data:", sensor_data)
        print("GPS:", location)

        decision = obstacle_avoidance(sensor_data)
        print("Decision:", decision)

        print("-" * 40)
        time.sleep(1)

if __name__ == "__main__":
    main()
