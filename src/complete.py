import point_readers
import metrics

class Complete:
    """docstring for Complete."""

    def __init__(self, filename, point_reader, dist):
        self.filename = filename
        self.path = '../input/' + filename

        file = open(self.path, 'r')
        points = point_reader(file)



c = Complete('euclidean-random-1000.in', point_readers.read_pts, metrics.euclidean)
