"""
Color sorting program for Dobot robotic arm.

This script controls a Dobot robotic arm to sort objects based on their colors using
a color sensor. It manages the conveyor belt movement, object pickup, color detection,
and sorting operations.

Functions:
    initialize_device(): Sets up and returns the Dobot device connection
    run_conveyor_belt(device, speed, direction, duration): Controls the conveyor belt movement
    detect_color(device): Detects the color of an object using the color sensor
    sort_object(device, color): Moves the object to its corresponding position based on color
    process_object(device): Handles the complete workflow for a single object
"""

from mydobot import MyDobot
from serial.tools import list_ports
import sys
import time

def initialize_device():
    """Initialize and return the Dobot device connection."""
    available_ports = list_ports.comports()
    if not available_ports:
        print("Error: No ports available. Please check your device connection.")
        sys.exit(1)
        
    print(f'available ports: {[x.device for x in available_ports]}')
    port = available_ports[0].device
    return MyDobot(port=port)

def run_conveyor_belt(device, speed=0.5, direction=1, duration=1):
    """
    Run the conveyor belt with specified parameters.
    
    Args:
        device: MyDobot instance
        speed: Belt speed between 0 and 1 (default: 0.5)
        direction: Movement direction, 1 or -1 (default: 1)
        duration: Run duration in seconds (default: 1)
    """
    device.conveyor_belt(speed=speed, direction=direction)
    time.sleep(duration)
    device.conveyor_belt(speed=0.0)  # Stop the belt

def detect_color(device):
    """
    Detect the color of an object using the color sensor.
    
    Returns:
        tuple: Color sensor readings (red, green, blue)
    """
    device.set_color_sensor(enable=True, port=0x01, version=0x1)
    time.sleep(1)  # Wait for color reading
    color = device.get_color_sensor()
    device.set_color_sensor(enable=False, port=0x01, version=0x1)
    return color

def sort_object(device, color):
    """
    Move object to appropriate position based on its color.
    
    Args:
        device: MyDobot instance
        color: Tuple of color sensor readings
    """
    if color[0] == 1:  # Red
        device.move_to(x=150, y=0, z=0)  # Red objects position
    elif color[1] == 1:  # Green
        device.move_to(x=0, y=150, z=0)  # Green objects position
    else:  # Other colors
        device.move_to(x=-150, y=0, z=0)  # Other objects position

def process_object(device):
    """Handle the complete process for a single object."""
    # Move to idle position
    device.move_to(x=0, y=0, z=0)
    
    # Pick up object
    device.suctioncup(on=True)
    device.move_to(x=100, y=50, z=50)
    
    # Move to color sensor
    device.move_to(x=-100, y=0, z=0)
    
    # Detect and sort
    color = detect_color(device)
    sort_object(device, color)
    
    # Release object
    device.suctioncup(on=False)

def main():
    """Main function to run the color sorting process."""
    try:
        device = initialize_device()
        
        # Process three objects
        for i in range(3):
            # Run conveyor belt longer for the first object
            duration = 5 if i == 0 else 1
            run_conveyor_belt(device, duration=duration)
            process_object(device)
            
        device.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()