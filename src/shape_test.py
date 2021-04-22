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

    # c_matrix = dbscan.read_file("../distances/shapes-500-complete.csv")
    # a1_matrix = dbscan.read_file("../distances/shapes-500-approx-eps-0.1.csv")
    # a3_matrix = dbscan.read_file("../distances/shapes-500-approx-eps-3.csv")
    #
    # embedding = dbscan.get_embedding(c_matrix)
    # epsilon = 0.4
    # true_labels = get_labels('./elliott-out.txt')
    #
    # dbc = dbscanner(c_matrix, epsilon)
    # dbc.run()
    # dbc.plot(embedding, title='Actual', true_labels=true_labels)
    #
    # dba1 = dbscanner(a1_matrix, epsilon)
    # dba1.run()
    # dba1.plot(embedding, title='Approx Epsilon - 0.1', true_labels=true_labels)
    #
    # dba3 = dbscanner(a3_matrix, epsilon)
    # dba3.run()
    # dba3.plot(embedding, title="Approx Epsilon - 3",true_labels=true_labels)
    #
    # homo, complete, v = sk.homogeneity_completeness_v_measure(dbc.labels, dba1.labels)
    # print("Approx (eps=0.1) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))
    #
    # homo, complete, v = sk.homogeneity_completeness_v_measure(dbc.labels, dba3.labels)
    # print("Approx (eps=3) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))
    # exit(13)

    eps = [10, 5, 3, 2, 1.5, 1, 0.5, 0.35, 0.1]
    printer_class.PRIORITY = 1  # no label ouptut
    graph = None
    lower = None
    upper = None
    for e in eps:
        a = run_approx(file, e, graph=graph, lower=lower, upper=upper)
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
