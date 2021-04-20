import math
import pickle

import numpy as np

from src.printer import printer


class Complete:
    """docstring for Complete."""

    def __init__(self, filename, point_reader, dist):
        self.filename = filename
        self.path = filename

        self.d = dist

        if filename.endswith('.pkl'):
            file = open(self.path, 'rb')
            self.points = pickle.load(file)
        else:
            self.points = point_reader(filename)  # create list of points using point_reader (assume point_reader returns list of points)

        printer("starting complete")
        self.build_matrix()  # compute n choose 2 different distances
        printer("ending complete")

    def build_matrix(self):
        n = len(self.points)
        matrix = np.zeros(shape=(n,n))  # initialize matrix
        for i in range(n):
            printer("Progress: " + str(i / n))
            for j in range(i,n):
                dist = self.d(self.points[i], self.points[j])
                # printer("finished frechet dist computation for ", sep="")
                matrix[i][j] = dist
                matrix[j][i] = dist
                print(str(j), end=", ", flush=True)
            print()



        self.matrix = matrix

    def mtx_to_file(self, path='NONE'):
        if path == 'NONE':
            filename = self.filename[:-3]  # chop off .in
        else:
            filename = path
        np.savetxt(filename + '-complete.csv', self.matrix, delimiter=",")





