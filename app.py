import cv2
from distance_meter import DistanceMeter

cap = cv2.VideoCapture(0)

dm = DistanceMeter(7, 50)

while True:

    ret, frame = cap.read()

    dm.find_marker(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
