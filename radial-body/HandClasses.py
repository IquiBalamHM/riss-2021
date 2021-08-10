# import the necessary packages
import numpy as np
import argparse
import cv2

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
      self.centerTriangle = [float(0),float(0)]
      for elem in centerlist:
        for point in elem:
          centerArray.append(point)
          self.centerTriangle[0] += point[0]
          self.centerTriangle[1] += point[1]
      self.centerTriangle[0] /= 3.0
      self.centerTriangle[1] /= 3.0
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
    self.HSVFiltered =  cv2.inRange(self.frame_HSV, self.low, self.high)
    self.FirstKernel = self.appykernel((3,3),self.HSVFiltered.copy())
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(self.FirstKernel.copy(), None, None, None, 8, cv2.CV_32S)

    #get CC_STAT_AREA component as stats[label, COLUMN] 
    areas = stats[1:,cv2.CC_STAT_AREA]

    self.result = np.zeros((labels.shape), np.uint8)

    for i in range(0, nlabels - 1):
        if areas[i] >= 70:   #keep
            self.result[labels == i + 1] = 255

    thresh = cv2.threshold(self.result,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    self.opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel2, iterations=1)
    
    cnts = cv2.findContours(self.opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
    current = self.opening.copy()
    self.centers = []
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

