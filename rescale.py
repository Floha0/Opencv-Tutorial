import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale) # 1 is the width
    height = int(frame.shape[0] * scale) # 0 is the height
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live video
    capture.set(3, width) # 3 for width
    capture.set(4, height) # 4 for height
    # 10 for brightness, 11 for contrast etc.

capture = cv.VideoCapture(0)
changeRes(640, 480)
while True:
    isTrue, frame = capture.read()
    # capture.read() returns 2 values, the first is a boolean if the frame is read correctly, the second is the frame itself

    if isTrue:
        cv.imshow('Video', frame)
    else:
        break

    if cv.waitKey(1) & 0xFF==ord('d'): # if the letter d is pressed
        break

capture.release()
cv.destroyAllWindows()