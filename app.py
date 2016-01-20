import cv2
from distance_meter import DistanceMeter

cap = cv2.VideoCapture(0)

dm = DistanceMeter(7, 50)

while True:

    ret, frame = cap.read()

    dimensions = dm.find_marker(frame)

    if dimensions is not None:

        if dm.focal_length == 0:
            dm.setup(dimensions[2])

        distance = dm.distance(dimensions[2])
        frame = dm.draw_marker(frame, dimensions, distance)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
