import pickle
import time

from datagen import genshapes
from src.approx import Approx
from src.complete import Complete
from src import point_readers, metrics, edge_selectors, dbscan
from src.printer import file_printer
from src.dbscan import dbscanner
import sklearn.metrics as sk
import sys

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d as plt3


def run_complete(file, path=""):
    s = time.time()
    c = Complete(file, point_readers.trip_r, metrics.frechet)
    file_printer("Complete: " + str(time.time() - s))
    if path == "":
        c.mtx_to_file(path="../distances/athens-small")
    else:
        c.mtx_to_file(path=path)


def run_approx(file, eps, path="", graph=None, lower=None, upper=None):
    s = time.time()
    a = Approx(file, eps, point_readers.trip_r, metrics.frechet, edge_selectors.blind_greedy,
               graph=graph, lower=lower, upper=upper)
    file_printer("Approx Eps {:f}: {:f}".format(eps,time.time() - s))
    if path == "":
        a.mtx_to_file(path="../distances/athens-small")
    else:
        a.mtx_to_file(path=path)
    return a


if __name__ == "__main__":

    path = "../distances/athens-small-"

    c_matrix = dbscan.read_file(path + "complete.csv")

    embedding = dbscan.get_embedding(c_matrix)
    epsilon = 1200
    # true_labels = get_labels('./elliott-out.txt')

    dbc = dbscanner(c_matrix, epsilon)
    dbc.run()
    dbc.plot(embedding, title='Actual', save='../plots/frechet/complete.png')

    out = "Epsilon, Homogeneity, Complete, V-Score\n"

    eps = [10, 5, 3, 2, 1.5, 1, 0.5, 0.35, 0.1]
    for e in eps:
        a_matrix = dbscan.read_file(path + "approx-eps-" + str(e) + ".csv")
        dba = dbscanner(a_matrix, epsilon)
        dba.run()
        dba.plot(embedding, title="Approx Epsilon - " + str(e), save='../plots/frechet/approx-' + str(e) + '.png')

        homo, complete, v = sk.homogeneity_completeness_v_measure(dbc.labels, dba.labels)
        out += "{:3f}, {:f}, {:f}, {:f}\n".format(e, homo, complete, v)
        print("Approx (eps={:3f}) clustering diff: {:f}, {:f}, {:f}".format(e, homo, complete, v))

    file_csv = open('../plots/frechet/values.csv', 'w')
    file_csv.write(out)
    file_csv.close()
    exit(13)

    '''
    RUN TESTS
    '''

    file = '../gps-data/athens_small/trips/'
    run_complete(file)


    eps = [10, 5, 3, 2, 1.5, 1, 0.5, 0.35, 0.1]
    graph = None
    lower = None
    upper = None
    for e in eps:
        a = run_approx(file, e, graph=graph, lower=lower, upper=upper)
        graph = a.G
        lower = a.lower
        upper = a.upper





    #db2.plot(a.points, title='Approx - 3')
