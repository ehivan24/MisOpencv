'''
Created on May 7, 2015

@author: edwingsantos
'''


'''

sift features with opencv

import cv2
import numpy as np

im = cv2.imread('99.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT()

kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('sift_points2.jpg', img)

print ('Done')

'''

import json
import os
import urllib, urlparse
import sift
from numpy import *
from PIL import Image
from pylab import *
import warp
from scipy import ndimage

'''
url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&set=public&from=0&to=20&minx=-77.037564&miny=38.896662&maxx=-77.035564&maxy=38.898662&size=medium'

c = urllib.urlopen(url)

j = json.loads(c.read())

imurls = []

for im in j['photos']:
    imurls.append(im['photo_file_url'])
    #print imurls.pop()



#Download images from the url

for url in imurls:
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))
    print 'downloading ->> ', url

    
## 

im = array(Image.open('empire.jpeg').convert('L'))
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))

figure()
gray()
imshow(im2)
#imshow(im)
show()
'''

im1 = array(Image.open('view.jpeg').convert('L'))
im2=  array(Image.open('99.jpg').convert('L'))


tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im1 = ndimage.affine_transform(im1,H[:2,:2],(H[0,2],H[1,2]))
im3 = warp.image_in_image(im1, im2, tp)

figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()






