import networkx as nx
import numpy as np
import time
import matplotlib.pyplot as plt

class Approx:
    def __init__(self, filename, eps, point_reader, dist, edge_selector):
        self.filename = filename
        self.path = '../input/' + filename

        self.epsilon = eps
        self.selector = edge_selector

        self.d = dist
        file = open(self.path, 'r')
        self.points = point_reader(file)  # create list of points using point_reader (assume point_reader returns list of points)
        file.close()

        self.init_graph()
        self.compute_spanner()
        self.build_matrix()

    def init_graph(self):
        n = len(self.points)
        self.lower = np.zeros((n,n))
        self.upper = np.inf * np.ones((n,n))
        for i in range(0,n):
            self.upper[i][i] = 0.0

        self.G = nx.Graph()
        self.G.add_nodes_from([i for i in range(n)])  # init G to be un-connected graph of n nodes

    def compute_spanner(self):
        indx = self.selector(self.lower, self.upper, self.epsilon)
        iter = 0
        while (indx[0] != -1):
            print("iter: " + str(iter))
            iter += 1
            i = indx[0]
            j = indx[1]
            s = time.time()
            dist = self.d(self.points[i], self.points[j])
            # print("Dist: " + str(time.time() - s))
            s = time.time()
            self.G.add_edge(i, j, weight=dist)
            # print("Add Edge: " + str(time.time() - s))
            s = time.time()
            self.update_bounds(dist, i, j)
            # print("Update Bounds: " + str(time.time() - s))
            s = time.time()
            indx = self.selector(self.lower, self.upper, self.epsilon)
            # print("Selector: " + str(time.time() - s))

    def update_bounds(self, v, i, j):
        n = len(self.points)
        self.lower[i][j] = v
        self.lower[j][i] = v
        self.upper[i][j] = v
        self.upper[j][i] = v

        for k in range(n):
            for l in range(n):
                if k == l:
                    continue

                # TODO: fix updates. Something is wrong with first coordinate. For [i][j] lower > upper sometimes and
                # TODO: if so then lower[i][k] = lower[i][q]

                upper = min(self.upper[k][l], self.upper[k][i] + v + self.upper[j][l], self.upper[k][j] + v + self.upper[i][l])
                self.upper[k][l] = upper
                # self.upper[l][k] = upper

                lower1 = v - self.upper[k][i] - self.upper[l][j]
                lower2 = v - self.upper[k][j] - self.upper[l][i]
                lower3 = self.lower[j][l] - v - self.upper[k][i]
                lower4 = self.lower[i][l] - v - self.upper[k][j]
                lower5 = self.lower[j][k] - v - self.upper[j][i]
                lower6 = self.lower[i][k] - v - self.upper[i][j]
                lower = max(self.lower[k][l],lower1,lower2,lower3,lower4,lower5,lower6)
                self.lower[k][l] = lower

    def build_matrix(self):
        n = len(self.points)
        print('Check correctness')
        bad = 0
        for i in range(n):
            for j in range(n):
                if self.upper[i][j] != self.lower[i][j]:
                    print("BAD AT " + str(i) + ', ' + str(j))
                    print(self.upper[i][j]/self.lower[i][j])
                    print(self.upper[i][j],self.lower[i][j])
                    bad += 1



        self.matrix = np.zeros((n,n))

        p = dict(nx.shortest_path_length(self.G, weight='weight'))
        print(p)

        print()
        print("Total Bad: " + str(bad))

        for i in range(n):
            for j in range(i, n):
                self.matrix[i][j] = p[i][j]
                self.matrix[j][i] = p[i][j]

    def mtx_to_file(self):
        filename = self.filename[:-3]  # chop off .in
        np.savetxt('../distances/' + filename + '-approx.csv', self.matrix, delimiter=",")
