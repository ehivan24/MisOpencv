'''
Created on Apr 17, 2015

@author: edwingsantos
'''

# Track objects in webcam based on Hue value. 
# Use object position to control cursor on macbook
# Optimised to track yellow beak of rubber duck!
# ctrl+c  Quits program
# robbierickman.blogspot.com


import cv2 
import sys 
from pylab import *

#    Convert image to HSV and threshold to produced binary image based on Hue value.
def thresholdImage(img):
    #allocate temp image based on size of input img
    img_hsv = cv2.cv.CreateImage((img.width,img.height),8,3)   #3 channel
    img_thresh = cv2.cv.CreateImage((img.width,img.height),8,1)#1 channel

    cv2.cv.CvtColor(img, img_hsv, cv2.cv.CV_BGR2HSV)    
    cv2.cv.InRangeS(img_hsv, cv2.cv.Scalar(5, 100, 100), cv2.cv.Scalar(30, 255, 255), img_thresh);
    
    return(img_thresh)
    
#    Plot a histogram showing Hue vs Saturation.  Not necessary for function of program, useful for optimising image thresholds
#    Samples from box in top corner of camera image only.
def histogram(src):
    # Set ccd sampling region.
    cv2.cv.SetImageROI(src,(10,10,100,100))
    
    # Convert to HSV
    hsv = cv2.cv.CreateImage(cv2.cv.GetSize(src), 8, 3)

    cv2.cv.CvtColor(src, hsv, cv2.cv.CV_BGR2HSV)
    s_plane = cv2.cv.CreateMat(cv2.cv.GetSize(src)[1], cv2.cv.GetSize(src)[0], cv2.cv.CV_8UC1)
    h_plane = cv2.cv.CreateMat(cv2.cv.GetSize(src)[1], cv2.cv.GetSize(src)[0], cv2.cv.CV_8UC1)
    


    cv2.cv.Split(hsv, h_plane, s_plane, None, None)
    planes = [h_plane, s_plane]

    h_bins = 28
    s_bins = 5
    hist_size = [h_bins, s_bins]
    # hue varies from 0 (~0 deg red) to 180 (~360 deg red again */
    h_ranges = [30, 180]
    # saturation varies from 0 (black-gray-white) to
    # 255 (pure spectrum color)
    s_ranges = [0, 255]
    ranges = [h_ranges, s_ranges]
    scale = 15
    
    
    # calculate histogram
    hist = cv2.cv.CreateHist([h_bins, s_bins], cv2.cv.CV_HIST_ARRAY, ranges, 1)
    cv2.cv.CalcHist([cv2.cv.GetImage(i) for i in planes], hist)
    (_, max_value, _, _) = cv2.cv.GetMinMaxHistValue(hist)
    
    # Reset cv sampling region to full CCD Area
    cv2.cv.ResetImageROI(src)


    # plot histogram data
    hist_img = cv2.cv.CreateImage((h_bins*scale, s_bins*scale), 8, 3)

    for h in range(h_bins):
        for s in range(s_bins):
            bin_val = cv2.cv.QueryHistValue_2D(hist, h, s)
            intensity = cv2.cv.Round(bin_val * 255 / max_value)
            cv2.cv.Rectangle(hist_img,(h*scale, s*scale),((h+1)*scale - 1, (s+1)*scale - 1),cv2.cv.RGB(intensity, intensity, intensity),cv2.cv.CV_FILLED)
    return hist_img

    

    


    
#    Filter noisy pixels using custom kernel size. 
#    Removes visually insignificant noise such as speckles
def erodeImage(img):
    kernel = cv2.cv.CreateStructuringElementEx(9,9,5,5, cv2.cv.CV_SHAPE_CROSS) 
    # Erode- replaces pixel value with lowest value pixel in kernel
    cv2.cv.Erode(img,img,kernel,2)
    # Dilate- replaces pixel value with highest value pixel in kernel
    cv2.cv.Dilate(img,img,kernel,2)
    return img
    
def contour_iterator(contour):
                while contour:
                        yield contour
                        contour = contour.h_next()
                        
    
def findImageContour(img,frame):
    storage = cv2.cv.CreateMemStorage()
    cont = cv2.cv.FindContours(img, storage,cv2.cv.CV_RETR_EXTERNAL,cv2.cv.CV_CHAIN_APPROX_NONE,(0, 0))
    max_center = [None,0]
    for c in contour_iterator(cont):
    # Number of points must be more than or equal to 6 for cv.FitEllipse2
    # Use to set minimum size of object to be tracked.
        if len(c) >= 60:
            # Copy the contour into an array of (x,y)s
            PointArray2D32f = cv2.cv.CreateMat(1, len(c), cv2.cv.CV_32FC2)
            for (i, (x, y)) in enumerate(c):
                PointArray2D32f[0, i] = (x, y)
                # Fits ellipse to current contour.
                (center, size, angle) = cv2.cv.FitEllipse2(PointArray2D32f)
                # Only consider location of biggest contour  -- adapt for multiple object tracking
            if size > max_center[1]:
                max_center[0] = center
                max_center[1] = size
                angle = angle
                        
            if True:
                # Draw the current contour in gray
                gray = cv2.cv.CV_RGB(255, 255, 255)
                cv2.cv.DrawContours(img, c, gray, gray,0,1,8,(0,0))
                        
    if max_center[1] > 0:
        # Convert ellipse data from float to integer representation.
        center = (cv2.cv.Round(max_center[0][0]), cv2.cv.Round(max_center[0][1]))
        size = (cv2.cv.Round(max_center[1][0] * 0.5), cv2.cv.Round(max_center[1][1] * 0.5))
        color = cv2.cv.CV_RGB(255,0,0)
        
        cv2.cv.Ellipse(frame, center, size,angle, 0, 360,color, 3, cv2.cv.CV_AA, 0)
       
    



def main():
    # create windows for use later
    cv2.cv.NamedWindow("LaserDuckOut",1)
    cv2.cv.NamedWindow("Theshold_IMG",1)
    cv2.cv.NamedWindow("HSV Histogram",1)
    # initiate camera
    capture = cv2.cv.CreateCameraCapture(0)
    
    # grab frame from camera
    if capture:
        while True:
            frame = cv2.cv.QueryFrame(capture)
            if not frame:
                cv2.cv.WaitKey(0)
                break
                
            cv2.cv.Flip(frame, frame,1)
            
            hist = histogram(frame)

            img = thresholdImage(frame)
            img = erodeImage(img)

            findImageContour(img,frame)
            
            
            # Mark out sampling region for histogram
            cv2.cv.Rectangle(frame,(10,10),(110,110),(0,255,0),1,0)


            # outputs image to windows created previously
            cv2.cv.ShowImage("Threshold_IMG",img)
            cv2.cv.ShowImage("LaserDuckOut",frame)
            cv2.cv.ShowImage("HSV_Histogram",hist)
                        
            if cv2.cv.WaitKey(10) >= 0:
                break
                
    cv2.cv.DestroyWindow("LaserDuckOut")
    cv2.cv.DestroyWindow("Threshold_IMG")
    cv2.cv.DestroyWindow("HSV_Histogram")
            







if __name__=='__main__':
    main()