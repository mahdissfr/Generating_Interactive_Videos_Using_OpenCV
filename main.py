import cv2
import math

image = cv2.imread('drop.jpg', 1)
cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)
fgbg = cv2.createBackgroundSubtractorMOG2()
frameRate = cap.get(5)  # frame rate

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    fgmask = fgbg.apply(frame)


    for i in range(0, int(width/10)):
        cv2.circle(frame, (i*(1+10), 30), 2, (255, 0, 0), 2)

    cv2.imshow('Input', frame)
    # cv2.imshow('frame', fgmask)

    # if (frameId % math.floor(frameRate) == 0):
    #     cv2.imwrite('output.jpg', frame)

    c = cv2.waitKey(30)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
