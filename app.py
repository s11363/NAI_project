import cv2
import imutils
from distance_meter import DistanceMeter

cap = cv2.VideoCapture(0)

dm = DistanceMeter(7, 50)

while True:

    ret, frame = cap.read()

    dimensions = dm.find_marker(frame)

    if dimensions is not None:
        frame = dm.draw_marker(frame, dimensions)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
