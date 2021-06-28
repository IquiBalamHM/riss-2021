import cv2

class Camera:
    def getFrame(self):
        if self.camera == 'WebCam':
            success, image = self.cap.read()
            return success,image

    def __init__(self,selection = "Web-Cam"):
        if selection== 'Intel':
            self.camera = 'Intel'
        else:
            self.cap = cv2.VideoCapture(0)
            self.camera = 'WebCam'