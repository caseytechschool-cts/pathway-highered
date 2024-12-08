from mydobot import MyDobot
from serial.tools import list_ports
import sys

try:
    available_ports = list_ports.comports()
    if not available_ports:
        print("Error: No ports available. Please check your device connection.")
        sys.exit(1)
        
    print(f'available ports: {[x.device for x in available_ports]}')
    port = available_ports[0].device
    device = MyDobot(port=port)
    device.move_to(x=100, y=50, z=50)
    device.close()
except Exception as e:
    print(f"An error occurred: {e}")