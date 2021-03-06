import os

import numpy as np
import glob
from src.printer import printer, file_printer
import src.printer as printer_class


def euclidean_r(file):
    file = open(file, 'r')
    points = []
    size = int(file.readline())
    for line in file:
        line = line.split(',')
        p = [float(l) for l in line]  # convert line to list of floats
        p = np.array(p)
        points.append(p)
    file.close()
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
    file.readline()  # read 'OFF\n'
    verts, face, edges = file.readline().split(' ')  # two headers in the OFF files
    face, verts, edges = int(face), int(verts), int(edges)
    points = []
    for _ in range(verts):
        line = file.readline().split(' ')
        p = [float(l) for l in line]  # convert line to list of floats
        p = np.array(p)
        points.append(p)
    return points


def shape_r(path, subdir='/'):
    points = []
    path = path
    dirs = next(os.walk(path))[1]
    printer(str(dirs))

    for dir in dirs:
        subpath = path + dir + subdir
        files = next(os.walk(subpath))[2]
        printer(str(dir))
        for f in files:
            file_printer("LABEL: {:} FILE: {:}".format(str(dir), str(f)), prio=0)
            points.append(read_model(subpath + f))

        printer_class.PRIORITY = 1


    printer("Done loading points")
    return points


def read_trip_file(file_name):
    points = []
    fin = open(file_name, "r")
    for line in fin:
        line = line.split(" ")
        points.append(np.array([float(line[0]), float(line[1])]))
    fin.close()
    return np.array(points)


def trip_r(dir):
    points = []
    files = glob.glob(dir + "/*.txt")
    for file in files:
        points.append(read_trip_file(file))
    return points
