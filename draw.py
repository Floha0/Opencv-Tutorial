import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # uint8 is a data type for images
# 3 stands for color channels

cv.imshow('Blank', blank)

# 1. Paint
blank[125:250] = 0,255,0
blank[200:350, 400:450] = 255,50,150
cv.imshow('Green', blank)

# 2. Rectangle
cv.rectangle(blank, (25,25), (blank.shape[1]//2, blank.shape[0]//2), (50,0,50), thickness=cv.FILLED) # cv.FILLED = -1
# // is integer division
# blank.size returns the number of pixels, not like shape which returns the dimensions (height, width, channels)
# img, pt1=origin, pt2=size, color, thickness
cv.imshow('Rectangle', blank)

# 3. Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,100,100), thickness=-1)
# img, center, radius, color, thickness
cv.imshow('Circle', blank)

# 4. Line
cv.line(blank, (int(blank.shape[1]-50), 15), (150, 450), (255,255,255), thickness=3)
# imgm, pt1=origin, pt2=destination, color, thickness
cv.imshow('Line', blank)

# 5. Text
cv.putText(blank, 'Sample', (75,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
# img, text, origin, font type, font scale, color, thickness
cv.imshow('Text', blank)

cv.waitKey(0)