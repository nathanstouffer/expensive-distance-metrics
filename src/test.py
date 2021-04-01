from src.approx import Approx
from src.complete import Complete
from src import point_readers, metrics, selectors
from src.dbscan import dbscanner

if __name__ == "__main__":
    c = Complete('euclidean-cluster-4-100.in', point_readers.euclidean_r, metrics.euclidean)
    c.mtx_to_file()
    db = dbscanner(c.matrix)
    db.run()
    db.plot(c.points)
    print()

    a = Approx('euclidean-cluster-4-100.in', 0, point_readers.euclidean_r, metrics.euclidean, selectors.blind_random)
    a.mtx_to_file()
    db2 = dbscanner(a.matrix)
    db2.run()
    db.plot(a.points)
