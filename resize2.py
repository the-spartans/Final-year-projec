# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:59:40 2020

@author: Harish
"""

from PIL import Image
from resizeimage import resizeimage

fd_img = open(r'C:\Users\Harish\Desktop\Plant project repo\plant-project\code\test6.jpg', 'r')
img = Image.open(fd_img)
img = resizeimage.resize_thumbnail(img, [200, 200])
img.save('test-image-thumbnail.jpeg', img.format)
fd_img.close()