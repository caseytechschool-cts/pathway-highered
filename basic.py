"""
This code block handles the connection and basic movement control of a Dobot robotic arm.

It performs the following operations:
1. Scans for available serial ports using list_ports.comports()
2. Checks if any ports are available, exits if none found
3. Automatically selects the first available port
4. Initializes the Dobot device with the selected port
5. Moves the robotic arm to a specific coordinate (x=100, y=50, z=50)
6. Properly closes the device connection

The code includes error handling to catch and display any exceptions that might occur
during the execution process.

Returns:
    None

Raises:
    Exception: If any error occurs during port connection or robot movement
"""
from mydobot import MyDobot
from serial.tools import list_ports
import sys

def main():
    try:
        available_ports = list_ports.comports()
        if not available_ports:
            print(f'Error: No ports available. Please check your device connection.')
            sys.exit(1)
            
        print(f'available ports: {[x.device for x in available_ports]}')
        port = available_ports[0].device
        device = MyDobot(port=port)
        device.move_to(x=100, y=50, z=50)
        device.close()
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()