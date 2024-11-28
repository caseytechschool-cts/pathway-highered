from mydobot import MyDobot
from serial.tools import list_ports

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

port = available_ports[0].device

device = MyDobot(port=port)

device.move_to(x=100, y=50, z=50)

device.close()