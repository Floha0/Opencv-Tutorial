import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# if the pixel value is greater than 125, it is set to 255 (white), otherwise 0 (black)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETR_LIST retrieves all the contours 
# RETR_EXTERNAL retrieves only the external contours
# RETR_TREE retrieves all the contours and creates a full family hierarchy list
# CHAIN_APPROX_NONE stores all the boundary points
# CHAIN_APPROX_SIMPLE stores only the end points
print(f"contours length: {len(contours)}")

cv.drawContours(blank, contours, -1, (0,0,255), 1)
# -1 means draw all the contours
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
