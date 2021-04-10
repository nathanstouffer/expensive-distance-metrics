import time

from src.approx import Approx
from src.complete import Complete
from src import point_readers, metrics, edge_selectors, dbscan
from src.dbscan import dbscanner
import sklearn.metrics as sk


if __name__ == "__main__":
    '''
    Load data
    '''
    matrix = dbscan.read_file('../distances/hausdorff-cloud-cluster-4-100-20-complete.csv')
    db = dbscanner(matrix, 10)
    db.run()
    db.plot(matrix, title='Actual')

    matrix = dbscan.read_file('../distances/hausdorff-cloud-cluster-4-100-20-approx-eps-0.1.csv')
    db = dbscanner(matrix, 10)
    db.run()
    db.plot(matrix, title='Epsilon = 0.1')

    matrix = dbscan.read_file('../distances/hausdorff-cloud-cluster-4-100-20-approx-eps-3.csv')
    db = dbscanner(matrix, 10)
    db.run()
    db.plot(matrix, title='Epsilon = 0.3')
    exit(13)

    '''
    RUN TESTS
    '''

    file = 'hausdorff-cloud-cluster-4-100-20.in'

    s = time.time()
    c = Complete(file, point_readers.hausdorff_cloud_r, metrics.hausdorff_cloud)
    print("Complete: " + str(time.time() - s))
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
    a = Approx(file, 0.1, point_readers.hausdorff_cloud_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy)
    print("Approx (eps=0.1): " + str(time.time() - s))
    a.mtx_to_file()
    db2 = dbscanner(a.matrix,10)
    db2.run()
    db2.plot(a.matrix, title="Epsilon = 0.1")

    homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    print("Approx (eps=0.1) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))

    #db2.plot(a.points, title='Approx - 0.1')

    s = time.time()
    a = Approx(file, 3, point_readers.hausdorff_cloud_r, metrics.hausdorff_cloud, edge_selectors.blind_greedy)
    print("Approx (eps=3): " + str(time.time() - s))
    a.mtx_to_file()
    db2 = dbscanner(a.matrix,10)
    db2.run()
    db2.plot(a.matrix, title="Epsilon = 3")

    homo, complete, v = sk.homogeneity_completeness_v_measure(db.labels, db2.labels)
    print("Approx (eps=3) clustering diff: {:f}, {:f}, {:f}".format(homo, complete, v))

    #db2.plot(a.points, title='Approx - 3')
