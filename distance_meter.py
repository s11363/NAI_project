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

        dimensions = None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.blur(gray, (3, 3))
        edge = cv2.Canny(gray, 55, 190)

        (derp, cnts, _) = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            curves = cv2.approxPolyDP(c, 0.02 * perimeter, True)

            if len(curves) == 4:
                (x, y, w, h) = cv2.boundingRect(curves)
                ratio = w / float(h)

                if 0.9 <= ratio <= 1.1:
                    dimensions = (x, y, w, h)
                    break

        return dimensions

    def draw_marker(self, frame, dimensions):

        (x, y, w, h) = dimensions

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return frame
