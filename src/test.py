from src.approx import Approx
from src.complete import Complete
from src import point_readers, metrics, edge_selectors
from src.dbscan import dbscanner

if __name__ == "__main__":
    # c = Complete('euclidean-cluster-4-100.in', point_readers.euclidean_r, metrics.euclidean)
    # c.mtx_to_file()
    # db = dbscanner(c.matrix,10)
    # db.run()
    # db.plot(c.points, title='Actual')
    # print()

    a = Approx('euclidean-cluster-4-100.in', 0.1, point_readers.euclidean_r, metrics.euclidean, edge_selectors.blind_greedy)
    a.mtx_to_file()
    db2 = dbscanner(a.matrix,10)
    db2.run()
    db2.plot(a.points, title='Approx - 0.1')
