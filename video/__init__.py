import cv2
import numpy as np
import glob


class ImageCapture:
    def __init__(self, capturedevice=0):
        self.cam = cv2.VideoCapture(0)
        self.image = None

    def capture(self):
        result, self.image = self.cam.read()

    def save(self, name):
        self.capture()
        cv2.imwrite(name, self.image)
        
 
class Video:
    def __init__(self, path=".", ext="png", output="video.avi"):
        img_array = []
        size = None
        for filename in sorted(glob.glob(f'{path}/*{ext}')):
            img = cv2.imread(filename)
            print(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
        out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
