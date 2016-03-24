'''
Created on May 3, 2015

@author: edwingsantos
'''
from cv2 import VideoCapture

"""import cv2
grayImage = cv2.imread('99.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('myPicGray.jpg', grayImage)

print ("Done")


#generates a picture with random pixels
import cv2
import numpy
import os

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)
print "done"
"""
"""
import cv2
videoCapture = VideoCapture('sample.mov')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)

size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('out.avi', cv2.cv.CV_FOURCC('1', '4', '2', '0'), fps, size)
success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()
    
"""

import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.cv.CV_EVENT_FLAG_LBUTTON:
        clicked = True
        
        
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Window')
cv2.setMouseCallback('Window', onMouse)

print 'Showing Camara feed. clicked Window. Any key to stop'



success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Window', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('Window')


















    