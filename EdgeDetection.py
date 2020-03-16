import HSVConvertGreen
import HSVConvertDisease
import os
import numpy as np
from skimage.io import imread, imshow
from skimage.filters import prewitt_h,prewitt_v
import matplotlib.pyplot as plt
import cv2
import cv
#%matplotlib inline

#reading the image
#os.system(HSVConvertGreen.py)
image = imread(r'test1.jpg',as_gray=True)
#image = imread(r'test1.jpg')
#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#calculating horizontal edges using prewitt kernel
edges_prewitt_horizontal = prewitt_h(image)
#calculating vertical edges using prewitt kernel5
edges_prewitt_vertical = prewitt_v(image)

frame_green = cv2.imread(r'test1.jpg')
res1_green = cv2.bitwise_and(frame_green,frame_green, mask= edges_prewitt_vertical)

print(edges_prewitt_vertical)
#color_img = cv2.cvtColor(edges_prewitt_vertical, cv2.COLOR_GRAY2RGB)

cv2.imshow('image.jpg', edges_prewitt_vertical)
cv2.imshow('image1.jpg', res1_green)



