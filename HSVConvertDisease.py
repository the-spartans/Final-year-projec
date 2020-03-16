# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:53:43 2020

@author: Harish
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:14:20 2020

@author: Harish
"""

import cv2
import numpy as np

#def HSVConvertDisease():

    # Take each frame
frame_color = cv2.imread(r'resize.jpg') 
count_color = 0;
    # Convert BGR to HSV
hsv = cv2.cvtColor(frame_color, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
lower_color = np.array([0,0,0])
upper_color = np.array([30,225,225])

    # Threshold the HSV image to get only blue colors
mask_color = cv2.inRange(hsv, lower_color, upper_color)
count_color = np.sum(mask_color == 255)
    # Bitwise-AND mask and original image
res_color = cv2.bitwise_and(frame_color,frame_color, mask= mask_color)

print(count_color)
cv2.imwrite("frame_color.jpg", frame_color)
cv2.imwrite("mask_color.jpg", mask_color)
cv2.imwrite("result_color.jpg", res_color)
cv2.imshow('frame',frame_color)
cv2.imshow('mask',mask_color)
cv2.imshow('res',res_color)

