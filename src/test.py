import pickle
import time

from src.approx import Approx
from src.complete import Complete
from src import point_readers, metrics, edge_selectors, dbscan
from src.printer import file_printer
from src.dbscan import dbscanner
import sklearn.metrics as sk
import sys


if __name__ == "__main__":

    # p = point_readers.model_net10_r(15)
    #
    # f = open('../input/ModelNet10_pickl-15.pkl', 'wb')
    # pickle.dump(p, f)
    # # exit(13)

    # sys.stdout = open('out.txt', 'w')
    #
    # complete = dbscan.read_file("../gps-data/athens_small/tri-complete.csv")
    # approx = dbscan.read_file("../gps-data/athens_small/tri-approx-eps-3.csv")
    #
    # embed = dbscan.get_embedding(complete)
    #
    # dbc = dbscanner(complete, 1200)
    # dbc.run()
    # dbc.plot(embed, title="Complete")
    # print(max(dbc.labels))
    #
    # dba = dbscanner(approx, 1200)
    # dba.run()
    # dba.plot(embed, title="Approx 3")
    # print(max(dba.labels))
    #
    # exit()

    '''
    RUN TESTS
    '''

    file = '../gps-data/athens_small/trips/'


    s = time.time()
    c = Complete(file, point_readers.trip_r, metrics.frechet)
    file_printer("Complete: " + str(time.time() - s))
    c.mtx_to_file()
    db = dbscanner(c.matrix,10)
    db.run()
    # db.plot(c.points, title='Actual')
    db.plot(c.matrix, title='Actual')
    print()

    # a = Approx('euclidean-cluster-1000-200.in', 0, point_readers.euclidean_r, metrics.euclidean, edge_selectors.blind_greedy)
    # a.mtx_to_file()
    # db2 = dbscanner(a.matrix,10)
    # db2.run()
    # db2.plot(a.points, title='Actual')

    s = time.time()
    a = Approx(file, 3, point_readers.trip_r, metrics.frechet, edge_selectors.blind_greedy)
    print("Approx (eps=3): " + str(time.time() - s))
    a.mtx_to_file()
    db2 = dbscanner(a.matrix, 10)
    db2.run()
    db2.plot(a.matrix, title="Epsilon = 3")
    print("Finished Approx 3")

    homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    file_printer("Approx (eps=3) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))

    s = time.time()
    a = Approx(file, 0.1, point_readers.trip_r, metrics.frechet, edge_selectors.blind_greedy)
    file_printer("Approx (eps=0.1): " + str(time.time() - s))
    a.mtx_to_file()
    db2 = dbscanner(a.matrix,10)
    db2.run()
    db2.plot(a.matrix, title="Epsilon = 0.1")

    homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    file_printer("Approx (eps=0.1) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))

    #db2.plot(a.points, title='Approx - 0.1')





    #db2.plot(a.points, title='Approx - 3')
