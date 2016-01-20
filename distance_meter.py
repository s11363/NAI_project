class DistanceMeter:
    def __init__(self, initial_edge_size, initial_distance):
        self.initial_edge_size = initial_edge_size
        self.initial_distance = initial_distance

        self.focal_length = 0

    def setup(self, width):
        self.focal_length = (width * self.initial_distance) / self.initial_edge_size

    def distance(self, read_width):
        return (self.initial_edge_size * self.focal_length) / read_width
