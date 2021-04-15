import os

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



def read_model(file):
    file = open(file, 'r')
    file.readline()
    verts, face, edges = file.readline().split(' ')  # two headers in the OFF files
    face, verts, edges = int(face), int(verts), int(edges)
    points = []
    for _ in range(verts):
        line = file.readline().split(' ')
        p = [float(l) for l in line]  # convert line to list of floats
        p = np.array(p)
        points.append(p)
    return points


def model_net10_r():
    points = []
    path = '../ModelNet10/'
    dirs = next(os.walk(path))[1]
    printer(str(dirs))

    for dir in dirs:
        subpath = path + dir + '/train/'
        files = next(os.walk(subpath))[2]
        printer(str(dir))
        for file in files:
            points.append(read_model(subpath + file))

    printer("Done loading points")
    return points

