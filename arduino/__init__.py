from serial import Serial
import time

class Arduino:
    def __init__(self, serialport, speed):
        self.serial = Serial(port=serialport, baudrate=speed)
        time.sleep(0.3)
        
    def send_command(self, cmd):
        time.sleep(0.2)
        self.serial.write(cmd)       


class StepperMotor:
    def __init__(self, parent=None):
        self.parent = parent

    def turn(self):
        self.parent.send_command(b"turn")
        time.sleep(1)
        self.parent.send_command(b"stop")
        time.sleep(1)
