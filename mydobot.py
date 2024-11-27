from pydobotplus import Dobot
from pydobotplus.message import Message

class MyDobot(Dobot):
    def suctioncup(self, on):
        return self.suck(enable=on)

    def set_color_sensor(self, enable=True, port=0x01, version=0x1):
        return self.set_color(enable=enable, port=port, version=version)

    def get_color_sensor(self, port=0x01, version=0x1):
        return self.get_color(port=port, version=version)
    
    def set_photoelectric_sensor(self, enable=True, port=0x02, version=0x1):
        msg = Message()
        msg.id = 138
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.param.extend(bytearray([int(enable)]))
        msg.params.extend(bytearray([port]))
        msg.params.extend(bytearray([version]))
        return self._extract_cmd_index(self._send_command(msg))
    
    def get_photoelectric_sensor(self, port=0x02):
        return self.get_ir(port=port)
