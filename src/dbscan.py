from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
import colorsys


class dbscanner:
    def __init__(self, matrix):
        self.matrix = matrix

    def run(self):
        clustering = DBSCAN(eps=10, metric='precomputed')
        clustering.fit(self.matrix)
        labels = clustering.labels_
        self.labels = labels
        # print(labels)
        # self.plot(labels, complete)

    def plot(self, points):
        colors_d = self.__assign_colors(max(self.labels) + 1)
        colors = {}
        for i in range(max(self.labels) + 1):
            colors[i] = colors_d[i]  # turn into rgb list (matplotlib likes it that way)
        colors[-1] = 'k'

        cvec = [colors[label] for label in self.labels]

        x = [p[0] for p in points]
        y = [p[1] for p in points]

        plt.figure(figsize=(10,10))
        plt.scatter(x, y, c=cvec)
        plt.show()

    @staticmethod
    def __assign_colors(N):
        HSV_tuples = [(x * 1.0 / N, 1, 1) for x in range(N)]
        colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples))
        return colors