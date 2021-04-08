import numpy as np

from src.printer import printer


def euclidean_r(file):
    points = []
    size = int(file.readline())
    for line in file:
        line = line.split(',')
        p = [float(l) for l in line]  # convert line to list of floats
        p = np.array(p)
        points.append(p)
    return points


def hausdorff_cloud_r(file):
    points = []
    file.readline()
    for line in file:
        cluster = []
        line = line.rstrip().split(";")
        for pt in line:
            if pt == '':
                continue
            pt = pt.split(",")
            pt = [float(p) for p in pt]
            pt = np.array(pt)
            cluster.append(pt)
        points.append(np.array(cluster))
    printer("Done loading points")
    return points

