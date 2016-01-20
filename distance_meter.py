import cv2


class DistanceMeter:
    def __init__(self, initial_edge_size, initial_distance):
        self.initial_edge_size = initial_edge_size
        self.initial_distance = initial_distance

        self.focal_length = 0

    def setup(self, width):
        self.focal_length = (width * self.initial_distance) / self.initial_edge_size

    def distance(self, read_width):
        return (self.initial_edge_size * self.focal_length) / read_width

    def find_marker(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edge = cv2.Canny(gray, 45, 175)

        cv2.imshow('edge', edge)
