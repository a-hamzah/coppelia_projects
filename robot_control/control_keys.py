from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time
import keyboard  # Library to capture keyboard input

# Initialize CoppeliaSim Remote API Client
client = RemoteAPIClient()
sim = client.getObject('sim')  # Get simulation object

def get_handles():
    try:
        # Get robot's body, wheel, and camera handles
        robot_handle = sim.getObject('/PioneerP3DX')
        left_motor = sim.getObject('/PioneerP3DX/leftMotor')
        right_motor = sim.getObject('/PioneerP3DX/rightMotor')
        camera_handle = sim.getObject('/PioneerP3DX/cam')  # Camera handle
        return robot_handle, left_motor, right_motor, camera_handle
    except Exception as e:
        print(f"Error retrieving handles: {e}")
        exit()

# Initialize robot handles
robot_handle, left_motor, right_motor, camera_handle = get_handles()

# Set wheel velocity
def set_wheel_velocity(left_speed, right_speed):
    sim.setJointTargetVelocity(left_motor, left_speed)
    sim.setJointTargetVelocity(right_motor, right_speed)

def main():
    print("Simulation starting...")
    sim.startSimulation()
    time.sleep(2)  # Wait for simulation to stabilize

    try:
        print("Use W, A, S, D, X keys to control the robot. Press Q to quit.")
        while True:
            if keyboard.is_pressed('w'):
                # Move forward
                set_wheel_velocity(1.0, 1.0)
            elif keyboard.is_pressed('s'):
                # Move backward
                set_wheel_velocity(-1.0, -1.0)
            elif keyboard.is_pressed('a'):
                # Turn left
                set_wheel_velocity(-0.5, 0.5)
            elif keyboard.is_pressed('d'):
                # Turn right
                set_wheel_velocity(0.5, -0.5)
            elif keyboard.is_pressed('x'):
                # Stop the robot
                set_wheel_velocity(0, 0)
            elif keyboard.is_pressed('q'):
                # Quit the loop
                print("Exiting control...")
                break
            
            # Add a small delay to avoid high CPU usage
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        print("Stopping simulation...")
        set_wheel_velocity(0, 0)  # Ensure the robot stops
        sim.stopSimulation()

if __name__ == "__main__":
    main()
