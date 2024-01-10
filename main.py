from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QPixmap
from arduino import StepperMotor, Arduino
import sys
from video import ImageCapture, Video
from serial.tools.list_ports import comports
from ui import Ui_Turntable, Ui_dlgConfig
import os

ports = [port.device for port in comports()]



class ConfigWindow(QDialog, Ui_dlgConfig):
    def __init__(self, parent=None):
        super(ConfigWindow, self).__init__()
        self.parent = parent
        self.setupUi(self)
        for port in ports:
            self.cmbUSB.addItem(port)
        
    def portChanged(self):
        if self.parent.arduino is None:
            self.parent.arduino = Arduino(self.cmbUSB.currentText(), 9600)
            self.parent.stepper = StepperMotor(parent=self.parent.arduino)
        else:
            if self.cmbUSB.currentText != self.parent.arduino.serial:
                self.parent.arduino = Arduino(self.cmbUSB.currentText(), 9600)
                self.parent.stepper = StepperMotor(parent=self.parent.arduino)


class MainWindow(QDialog, Ui_Turntable):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.capture = ImageCapture()
        self.config = None
        self.arduino = None
        self.stepper = None
        self.setupUi(self)
        self.lblStatus.setText("")
        self.show()
        self.configure()

    def configure(self):
        if self.config is not None:
            self.config.close()

        self.config = ConfigWindow(self)
        self.config.show()
        
    def startCapture(self):
        i = 1
        os.system("rm image*png")
        nframes = self.config.spinFrames.value()
        while 1:
            fname = f"image{i:04}.png"
            self.capture.save(fname)
            self.lblCam.setPixmap(QPixmap(fname))
            self.lblStatus.setText(f"{i} of {nframes}")
            QApplication.processEvents()
            i+=1
            if i == self.config.spinFrames.value():
                vid = Video()
                sys.exit()
            self.stepper.turn()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)


