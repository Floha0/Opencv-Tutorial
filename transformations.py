import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')

cv.imshow('Group 1', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0) # 0 flips vertically, 1 flips horizontally, -1 flips both
cv.imshow('Flipped', flip)



cv.waitKey(0)