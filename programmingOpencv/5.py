'''
Created on May 11, 2015

@author: edwingsantos
'''

#https://github.com/jesolem/PCV/tree/master/examples

import cv2
from numpy import *

def drawFlow(im, flow, step=16):
    h,w = im.shape[:2]
    x,y = mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    fx, fy = flow[x,y].T
    
    lines = vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = int32(lines)
    
    vis =cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    
    for (x1,y1),(x2,y2) in lines:
        cv2.line(vis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(vis,(x1,y1),1,(0,255,0), -1) 
    
    return vis  


cap = cv2.VideoCapture(0)

ret, im = cap.read()
prevGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


while True:
    ret, im = cap.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    flow = cv2.calcOpticalFlowFarneback(prevGray,gray,None,0.5,3.0,15.0,3.0,5.0,1.2,0.0)
    prevGray =gray
    
    cv2.imshow('Cam Feed', drawFlow(gray,flow))
    if cv2.waitKey(10) == 27:
        break
    
    
    