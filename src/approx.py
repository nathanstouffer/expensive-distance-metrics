import pickle

import networkx as nx
import numpy as np
import time
import matplotlib.pyplot as plt

from src.printer import printer


class Approx:
    def __init__(self, filename, eps, point_reader, dist, edge_selector, graph=None, lower=None, upper=None):
        self.filename = filename
        self.path = filename

        self.epsilon = eps
        self.selector = edge_selector

        self.d = dist
        if filename.endswith('.pkl'):
            file = open(self.path, 'rb')
            self.points = pickle.load(file)
        else:
            self.points = point_reader(filename)

        printer("starting approx with eps=" + str(self.epsilon))
        self.init_graph()

        if graph is not None and lower is not None and upper is not None:
            self.lower = lower
            self.upper = upper
            self.G = graph

        self.compute_spanner()
        self.build_matrix()
        printer("ending approx with eps=" + str(self.epsilon))


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
            if iter % 100 == 0:
                printer("Iter: " + str(iter))
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
            for l in range(k+1, n):
                u1, u2, u3 = self.upper[k][l], self.upper[k][i] + v + self.upper[j][l], self.upper[k][j] + v + self.upper[i][l]
                upper = min(u1, u2, u3)
                # self.upper[l][k] = upper

                lower1 = v - self.upper[k][i] - self.upper[l][j]
                lower2 = v - self.upper[k][j] - self.upper[l][i]
                lower3 = self.lower[j][l] - v - self.upper[k][i]
                lower4 = self.lower[i][l] - v - self.upper[k][j]
                lower5 = self.lower[j][k] - v - self.upper[l][i]
                lower6 = self.lower[i][k] - v - self.upper[l][j]
                lower = max(self.lower[k][l],lower1,lower2,lower3,lower4,lower5,lower6)

                self.upper[k][l] = upper
                self.lower[k][l] = lower
                self.upper[l][k] = upper
                self.lower[l][k] = lower

                if self.lower[k][l] > self.upper[k][l]:
                    print("BAD")


    def build_matrix(self):
        n = len(self.points)
        self.matrix = np.zeros((n,n))

        p = dict(nx.shortest_path_length(self.G, weight='weight'))
        # print(p)

        for i in range(n):
            for j in range(i, n):
                self.matrix[i][j] = p[i][j]
                self.matrix[j][i] = p[i][j]

    def draw_graph(self, save="FALSE"):
        pos = nx.circular_layout(self.G)
        nx.draw(self.G, pos=pos, node_size=25, node_color='g', width=0.1)

        if save != "FALSE":
            plt.savefig(save)
        plt.show()

    def mtx_to_file(self, path='NONE'):
        if path == 'NONE':
            filename = self.filename[:-3]  # chop off .in
        else:
            filename = path
        np.savetxt(filename + '-approx-eps-' + str(self.epsilon) + '.csv', self.matrix, delimiter=",")
