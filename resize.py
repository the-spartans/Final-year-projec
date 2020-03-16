# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:51:43 2020

@author: Harish
"""
import cv2
 
img = cv2.imread(r'C:\Users\Harish\Desktop\Plant project repo\plant-project\code\test9.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
#scale_percent = 60 # percent of original size
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
width = 300
height = 300
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
cv2.imwrite("resize.jpg", resized)
cv2.imshow("Resized image", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()