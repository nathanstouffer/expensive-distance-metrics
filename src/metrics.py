import math
import numpy.linalg as la
import numpy as np


'''
Basic euclidean distance
'''
def euclidean(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    return la.norm(p1 - p2)


'''
Hausdorf distance between two point clouds
'''
def hausdorff_cloud(c1, c2):
    sup = float('-inf')
    for p in c1:
        inf = float('inf')
        for q in c2:
            d = euclidean(p, q)
            if d < inf:
                inf = d
        if inf > sup:
            sup = inf

    for p in c2:
        inf = float('inf')
        for q in c1:
            d = euclidean(p, q)
            if d < inf:
                inf = d
        if inf > sup:
            sup = inf

    return sup


