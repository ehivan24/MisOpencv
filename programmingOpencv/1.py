'''
Created on May 4, 2015

@author: edwingsantos


from PIL import  Image
import os

path = '/Users/edwingsantos/Documents/workspaceJava/MisOpencv/programmingOpencv/'

def getImages(path): 
    
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')] 


print getImages(path)
'''

from PIL import Image
from pylab import *
im = array(Image.open('99.jpg',).convert('L'))
figure()
gray()

contour(im, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(), 128)
show()

