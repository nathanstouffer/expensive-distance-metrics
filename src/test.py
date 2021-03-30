from src.complete import Complete
from src import point_readers, metrics





if __name__ == "__main__":
    c = Complete('euclidean-random-10.in', point_readers.euclidean_r, metrics.euclidean)
    c.mtx_to_file()
    print()