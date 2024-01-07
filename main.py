from PySide6.QtWidgets import QApplication, QDialog
from arduino import StepperMotor, Arduino
import sys
from video import ImageCapture, Video

from ui import Ui_Turntable


class MainWindow(QDialog, Ui_Turntable):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.capture = None
        
        self.setupUi(self)
        self.show()
        

    def startCapture(self):
        pass

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)


"""
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
    
"""
