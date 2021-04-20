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


if __name__ == "__main__":

    '''
    RUN TESTS
    '''

    file = '../gen_shapes/'

    s = time.time()
    c = Complete(file, point_readers.shape_r, metrics.hausdorff_cloud)
    file_printer("Complete: " + str(time.time() - s))
    c.mtx_to_file(path="../distances/shapes-500")
    # db = dbscanner(c.matrix, 1)
    # db.run()
    # # db.plot(c.points, title='Actual')
    # db.plot(c.matrix, title='Actual')
    print()

    s = time.time()
    a = Approx(file, 3, point_readers.shape_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy)
    file_printer("Approx (eps=3): " + str(time.time() - s))
    a.mtx_to_file(path="../distances/shapes-500")
    # db2 = dbscanner(a.matrix, 1)
    # db2.run()
    # db2.plot(a.matrix, title="Epsilon = 3")
    # print("Finished Approx 3")
    #
    # homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    # file_printer("Approx (eps=3) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))

    # s = time.time()
    # a = Approx(file, 0.1, point_readers.shape_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy)
    # file_printer("Approx (eps=0.1): " + str(time.time() - s))
    # a.mtx_to_file()
    # db2 = dbscanner(a.matrix,1)
    # db2.run()
    # db2.plot(a.matrix, title="Epsilon = 0.1")
    #
    # homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    # file_printer("Approx (eps=0.1) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))
