import cv2 as cv


""" 
Read Image
img = cv.imread('Photos/cat.jpg')   # return matrix of pixels

cv.imshow('Cat', img) # window name, image

cv.waitKey(0) # 0 means wait indefinitely for a key press
"""

# ------------------------------

"""
Read Video

"""
# integer for webcam, string for video file
capture = cv.VideoCapture(0)   
# capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    # capture.read() returns 2 values, the first is a boolean if the frame is read correctly, the second is the frame itself

    if isTrue:
        flip = cv.flip(frame, 1)
        cv.imshow('Video', flip)
    else:
        break

    if cv.waitKey(1) & 0xFF==ord('d'): # if the letter d is pressed
        break

capture.release()
cv.destroyAllWindows()