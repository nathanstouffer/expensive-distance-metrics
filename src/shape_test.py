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


def run_approx(file, eps, path=""):
    s = time.time()
    c = Approx(file, eps, point_readers.shape_r, metrics.hausdorff_cloud)
    file_printer("Approx Eps {:f}: {:f}".format(eps,time.time() - s))
    if path == "":
        c.mtx_to_file(path="../distances/shapes-500")
    else:
        c.mtx_to_file(path=path)


if __name__ == "__main__":

    '''
    RUN TESTS
    '''

    file = '../gen_shapes/'

    eps = [0.5, 1, 1.5, 2, 5]
    printer_class.PRIORITY = 1
    for e in eps:

        run_approx(file, e)


    run_complete(file)
    # db = dbscanner(c.matrix, 1)
    # db.run()
    # # db.plot(c.points, title='Actual')
    # db.plot(c.matrix, title='Actual')

    print()

    run_approx(file, 3)
    # db2 = dbscanner(a.matrix, 1)
    # db2.run()
    # db2.plot(a.matrix, title="Epsilon = 3")
    # print("Finished Approx 3")
    #
    # homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    # file_printer("Approx (eps=3) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))

    s = time.time()
    a = Approx(file, 0.1, point_readers.shape_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy)
    file_printer("Approx (eps=0.1): " + str(time.time() - s))
    a.mtx_to_file(path="../distances/shapes-500")
    # db2 = dbscanner(a.matrix,1)
    # db2.run()
    # db2.plot(a.matrix, title="Epsilon = 0.1")
    #
    # homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    # file_printer("Approx (eps=0.1) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))
