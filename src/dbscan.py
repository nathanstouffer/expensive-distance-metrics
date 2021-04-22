from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
import colorsys
from sklearn.manifold import MDS


class dbscanner:
    def __init__(self, matrix, ep):
        self.matrix = matrix
        self.epsilon = ep

    def run(self):
        clustering = DBSCAN(eps=self.epsilon, metric='precomputed')
        clustering.fit(self.matrix)
        labels = clustering.labels_
        self.labels = labels
        # print(labels)
        # self.plot(labels, complete)

    def plot(self, points, title = 'NONE', true_labels=None):
        if np.array(points).shape[1] > 2:  # we have a distance matrix so find an embedding
            points = get_embedding(points)

        colors_d = self.__assign_colors(max(self.labels) + 1)
        colors = {}
        for i in range(max(self.labels) + 1):
            colors[i] = colors_d[i]  # turn into rgb list (matplotlib likes it that way)
        colors[-1] = 'k'

        cvec = [colors[label] for label in self.labels]
        mvec, true = ['.' for _ in points], ['.' for _ in points]
        if true_labels is not None:
            mvec, true = self.__assign_shapes(true_labels)

        x = [p[0] for p in points]
        y = [p[1] for p in points]

        fig = plt.figure(figsize=(10,10))
        mtypes = list(set(mvec))
        for j,type in enumerate(mtypes):
            px = []
            py = []
            pc = []
            for i in range(len(points)):
                if (mvec[i] == type):
                    px.append(x[i])
                    py.append(y[i])
                    pc.append(cvec[i])
            plt.scatter(px, py, color=pc, marker=type, s=50, label=true[j])

        if title != 'NONE':
            plt.title(title)

        plt.legend()

        plt.show()

    @staticmethod
    def __assign_colors(N):
        HSV_tuples = [(x * 1.0 / N, 1, 1) for x in range(N)]
        colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples))
        return colors

    @staticmethod
    def __assign_shapes(labels):
        labs = list(set(labels))  # this is horrible
        markers = ['.', 'o', 'v', "s", "+", "D", "^", "p", "x", "*"]
        marks = []
        for l in labels:
            indx = labs.index(l)
            marks.append(markers[indx])
        return marks, labs



def read_file(filepath):
    arr = np.genfromtxt(filepath, delimiter=",")
    return arr


def get_embedding(matrix):
    model = MDS(n_components=2, dissimilarity='precomputed', random_state=1)
    out = model.fit_transform(matrix)
    points = []
    for p in out:
        point = (p[0], p[1])
        points.append(point)
    return points

