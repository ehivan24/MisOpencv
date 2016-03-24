'''
Created on Apr 16, 2015

@author: edwingsantos
'''


import numpy as np
import cv2
# opencv 2.41 - python 2.73

filename = "test.jpg" #http://3.bp.blogspot.com/-1UtLXb7c73U/T9QZT3tpVjI/AAAAAAAAATE/Nyo7SFg8T1o/s200/balls.png
im = cv2.imread(filename)
new = im.copy()

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,100,255,0) ## determinate objects
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("original image",im)
print "PULSE TO ANY KEY TO CONTINUE"

for h,cnt in enumerate(contours):
    
    mask = np.zeros(imgray.shape,np.uint8)
    cv2.drawContours(mask,[cnt],0,(255,255,0),-1)
    mean = cv2.mean(im,mask = mask) # calculate figure color

    key = cv2.waitKey(0)
    
    label = "silueta  %s "
    text = (label % (h))
    cv2.imshow(text, mask)
   
    maskc = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
    label2 = "figura  %s "
    text2 = (label2 % (h))
    cv2.drawContours(maskc,[cnt],0,(255,34,55),-1)
    cv2.imshow(text2, maskc)   

cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    pass