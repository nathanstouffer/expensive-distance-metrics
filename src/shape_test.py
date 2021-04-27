import pickle
import time

from datagen import genshapes
from src.approx import Approx
from src.complete import Complete
from src import point_readers, metrics, edge_selectors, dbscan
from src.printer import file_printer
from src import printer as printer_class
from src.dbscan import dbscanner
import sklearn.metrics as sk
import sys

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d as plt3


def run_complete(file, path=""):
    s = time.time()
    c = Complete(file, point_readers.shape_r, metrics.hausdorff_cloud)
    file_printer("Complete: " + str(time.time() - s))
    if path == "":
        c.mtx_to_file(path="../distances/shapes-500")
    else:
        c.mtx_to_file(path=path)


def run_approx(file, eps, path="", graph=None, lower=None, upper=None):
    s = time.time()
    a = Approx(file, eps, point_readers.shape_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy,
               graph=graph, lower=lower, upper=upper)
    file_printer("Approx Eps {:f}: {:f}".format(eps,time.time() - s))
    if path == "":
        a.mtx_to_file(path="../distances/shapes-500")
    else:
        a.mtx_to_file(path=path)
    return a


def get_labels(path):
    f = open(path, 'r')
    labs = []
    for line in f:
        if "LABEL:" in line:
            line = line.split("FILE:")[0].replace("LABEL:", "").strip()
            labs.append(line)
    return labs


if __name__ == "__main__":

    '''
    RUN TESTS
    '''

    file = '../gen_shapes/'

    path = "../distances/shapes-500-"

    c_matrix = dbscan.read_file(path + "complete.csv")

    embedding = dbscan.get_embedding(c_matrix)
    epsilon = 0.4
    true_labels = get_labels('./elliott-out.txt')

    dbc = dbscanner(c_matrix, epsilon)
    dbc.run()
    dbc.plot(embedding, title='Actual', true_labels=true_labels, save='../plots/shapes/complete.png')

    out = "Epsilon, Homogeneity, Complete, V-Score\n"

    eps = [10, 5, 3, 2, 1.5, 1, 0.5, 0.35, 0.1]
    for e in eps:
        a_matrix = dbscan.read_file(path + "approx-eps-" + str(e) + ".csv")
        dba = dbscanner(a_matrix, epsilon)
        dba.run()
        # embedding = dbscan.get_embedding(a_matrix)
        dba.plot(embedding, title="Approx Epsilon - " + str(e), true_labels=true_labels, save='../plots/shapes/approx-' + str(e) + '.png')

        homo, complete, v = sk.homogeneity_completeness_v_measure(dbc.labels, dba.labels)
        out += "{:3f}, {:f}, {:f}, {:f}\n".format(e, homo, complete, v)
        print("Approx (eps={:3f}) clustering diff: {:f}, {:f}, {:f}".format(e, homo, complete, v))

    file_csv = open('../plots/shapes/values.csv', 'w')
    file_csv.write(out)
    file_csv.close()
    exit(13)

    # a = Approx("../input/euclidean-cluster-4-100.in", 3, point_readers.euclidean_r, metrics.euclidean, edge_selectors.blind_greedy)
    # a.draw_graph(save="test.png")
    #
    # exit(13)

    """"compute approximate distance matrices"""

    eps = [10, 5, 3, 2, 1.5, 1, 0.5, 0.35, 0.1]
    printer_class.PRIORITY = 1  # no label ouptut
    graph = None
    lower = None
    upper = None
    for e in eps:
        a = run_approx(file, e, graph=graph, lower=lower, upper=upper)
        a.draw_graph(save="../plots/shape_graphs/approx-" + str(e) + ".png")
        graph = a.G
        lower = a.lower
        upper = a.upper

    exit(13)

    run_complete(file)

    print()

    run_approx(file, 3)

    s = time.time()
    a = Approx(file, 0.1, point_readers.shape_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy)
    file_printer("Approx (eps=0.1): " + str(time.time() - s))
    a.mtx_to_file(path="../distances/shapes-500")
