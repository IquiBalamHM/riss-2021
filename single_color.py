# import the necessary packages
import numpy as np
import argparse
import cv2

# define the list of boundaries
lowerblue = np.array([75, 79, 107])
higherblue = np.array([103,151,155])

loweryellow = np.array([29,58,146])
higheryellow = np.array([74,115,240])

lowerpurple = np.array([110,35,150])
higherpurple = np.array([159,147,218])

lowergreen = np.array([47,41,135])
highergreen = np.array([80,156,255])

lowernewgreen = np.array([57,41,231])
highernewgreen = np.array([93,140,255])
class HandClassOneColor:  
  def PolyArea2D(self,pts):
    lines = np.hstack([pts,np.roll(pts,-1,axis=0)])
    area = 0.5*abs(sum(x1*y2-x2*y1 for x1,y1,x2,y2 in lines))
    if area < 1200:
        self.state = 'Closed'
    else:
        self.state = 'Open'
    return area
  def __init__(self, centerlist):
    if (len(centerlist[0]))==3:
      self.flag = True  
    #if (len(centerlist[0])==1 and len(centerlist[1])==1 and len(centerlist[2])==1):
      self.numberofFingers = 3
      #self.index = centerlist[0]
      #self.middle = centerlist[1]
      #self.thumb = centerlist[2]
      centerArray = []
      for elem in centerlist:
        for point in elem:
          centerArray.append(point)
      self.area = self.PolyArea2D(centerArray)
    else:
      self.numberofFingers = 0
class HandClass:  
  def PolyArea2D(self,pts):
    lines = np.hstack([pts,np.roll(pts,-1,axis=0)])
    area = 0.5*abs(sum(x1*y2-x2*y1 for x1,y1,x2,y2 in lines))


  def __init__(self, centerlist):
    if (len(centerlist[0]) + len(centerlist[1]) + len(centerlist[2]))==3:
      self.flag = True  
    #if (len(centerlist[0])==1 and len(centerlist[1])==1 and len(centerlist[2])==1):
      self.numberofFingers = 3
      self.index = centerlist[0]
      self.middle = centerlist[1]
      self.thumb = centerlist[2]
      centerArray = []
      for elem in centerlist:
        for point in elem:
          centerArray.append(point)
      self.area = self.PolyArea2D(centerArray)
    else:
      self.numberofFingers = 0




class MaskClass:
  def __init__(self, frame_HSV, lowerbound,higherbound):
    self.frame_HSV = frame_HSV
    self.low = lowerbound
    self.high = higherbound
  def appykernel(self,kerneldim,mask):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,kerneldim)
    res = cv2.morphologyEx(mask.copy(),cv2.MORPH_OPEN,kernel,iterations = 3)
    return res
  def process(self):
    self.processed =  cv2.inRange(self.frame_HSV, self.low, self.high)
    self.processed2 = self.appykernel((3,3),self.processed.copy())
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(self.processed2.copy(), None, None, None, 8, cv2.CV_32S)

    #get CC_STAT_AREA component as stats[label, COLUMN] 
    areas = stats[1:,cv2.CC_STAT_AREA]

    self.result = np.zeros((labels.shape), np.uint8)

    for i in range(0, nlabels - 1):
        if areas[i] >= 70:   #keep
            self.result[labels == i + 1] = 255

    thresh = cv2.threshold(self.result,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    self.opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel2, iterations=3)
    cnts = cv2.findContours(self.opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    emptymask = np.zeros((self.opening.shape),dtype= np.uint8)
    blobs = 0
    arrayareas = []
    for c in cnts:
        area = cv2.contourArea(c)
        arrayareas.append(area)
        cv2.drawContours(emptymask, [c], -1, (36,255,12), -1)
        if area >450:
            blobs += 1
    self.centers = []
    current = self.opening.copy()
    # loop over the contours
    for c in cnts:
      # compute the center of the contour
      M = cv2.moments(c)
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
      # draw the contour and center of the shape on the image
      cv2.drawContours(current, [c], -1, (0, 255, 0), 2)
      cv2.circle(current, (cX, cY), 2, (255, 255, 255), -1)
      self.centers.append((cX,cY))
      #cv2.putText(current, "center", (cX - 20, cY - 20),
        #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    self.tagged = current

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    inputimage = cv2.flip(image.copy(),1)
    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image_rgb = image.copy()
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    #results = hands.process(image)

    # Draw the hand annotations on the image.
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    frame_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_height, image_width, _ = image.shape
    maskgreen = MaskClass(frame_HSV.copy(),lowernewgreen,highernewgreen)
    maskgreen.process()
    cv2.imshow('green',maskgreen.tagged)
    
    fullcenters = []
    fullcenters.append(maskgreen.centers)
    #fullcenters.append(maskyellow.centers)
    hand1 = HandClassOneColor(fullcenters)
    #print(len(fullcenters[0]))
    font = cv2.FONT_HERSHEY_PLAIN
    if hand1.numberofFingers == 3:
      print(str(hand1.area) + ' ' +str(hand1.state))
      cv2.putText(inputimage, 'Hand'+ str(hand1.state), (image_width-200,25), font, 2, (120,120,0), 3)
    else: 
      cv2.putText(inputimage, 'Not Right Hand', (image_width-300,25), font, 2, (120,120,0), 3)  

    masksum = maskgreen.tagged
    cv2.imshow('post',inputimage)

    #cv2.imshow('sum',masksum)
    bin = cv2.waitKey(5)
    if bin & 0xFF == ord('q'):
        break
    elif bin & 0xFF ==ord('s'):
        print('save')

cap.release()
# loop over the boundaries
