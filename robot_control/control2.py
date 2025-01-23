from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

client = RemoteAPIClient()
sim = client.getObject('sim')  # Get simulation object

def get_handles():
    try:
        # Get robot's body and wheel handles
        robot_handle = sim.getObject('/PioneerP3DX')
        left_motor = sim.getObject('/PioneerP3DX/leftMotor')
        right_motor = sim.getObject('/PioneerP3DX/rightMotor')
        return robot_handle, left_motor, right_motor
    except Exception as e:
        print(f"Error retrieving handles: {e}")
        exit()

# Initialize robot handles
robot_handle, left_motor, right_motor = get_handles()

# Set wheel velocity
def set_wheel_velocity(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

# Main function
def main():
    print("Simulation starting...")
    sim.startSimulation()
    time.sleep(2)  # Wait for simulation to stabilize

    try:
        # Move forward
        print("Moving in circles...")
        set_wheel_velocity(1.0, 1.0)
        time.sleep(5)

        # Stop the robot
        print("Stopping")
        set_wheel_velocity(0, 0)
        time.sleep(3)

        # Move backword
        print("Turning right")
        set_wheel_velocity(-1.0, -1.0)
        time.sleep(5)

        # Stop the robot
        print("Stopping")
        set_wheel_velocity(0, 0)

    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        print("Stopping simulation...")
        sim.stopSimulation()

if __name__ == "__main__":
    main()