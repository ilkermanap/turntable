from arduino import StepperMotor, Arduino
import sys
from video import ImageCapture, Video

capture = ImageCapture()

ard = Arduino('/dev/ttyUSB0', 9600)
step = StepperMotor(parent=ard)



i = 1
while 1:
    capture.save(f"image{i:04}.png")
    print(i)
    i+=1
    if i == 100:
        vid = Video()
        sys.exit()
    step.turn()
    
