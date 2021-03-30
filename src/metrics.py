import math
import numpy.linalg as la
import numpy as np


def euclidean(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return la.norm(p1 - p2)
