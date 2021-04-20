import random
import numpy as np
import math


def cube(n):
    points = []
    for _ in range(n):
        '''
        This generates points on a plane
        Which plane they are on depends on values of index, val
        eg index = 2 (z), val = 1, means points are on top face of cube
        '''
        x, y, z = (random.random() * 2 - 1), (random.random() * 2 - 1), (random.random() * 2 - 1)  # generate point inside cube
        p = np.array([x, y, z])
        index = random.choice([0, 1, 2])  # choose what face we are on (+ or - direction)
        val = random.choice([-1, 1])  # choose the face
        p[index] = val
        points.append(p)
    return points


def torus(n):
    R = 1
    r = 0.5
    points = []
    for _ in range(n):
        theta = 2 * math.pi * random.random()
        phi = 2 * math.pi * random.random()
        point = np.array([(R+r*math.cos(phi))*math.cos(theta), (R+r*math.cos(phi))*math.sin(theta), r*math.sin(phi)])
        points.append(point)
    return points

def pyramid(n):
    points = []
    for _ in range(n):
        face_select = random.random()
        if face_select < 0.2:  # on the bottom
            x, y, z = (random.random() * 2 - 1), (random.random() * 2 - 1), -1
            p = np.array([x, y, z])
            points.append(p)
            continue

        # We are on side of pyramid
        z = (random.random() * 2 - 1)  # choose our z level on pyramid
        side_length = 1 - z  # size of square cross-section
        x, y = (random.random() * side_length - side_length/2), (random.random() * side_length - side_length/2)  # compute points on square at z level

        p = np.array([x, y, z])
        index = random.choice([0, 1])  # choose what face we are on (+ or - direction)
        val = random.choice([-side_length, side_length])  # choose the face
        p[index] = val
        points.append(p)
    return points


def sphere(n):
    points = []
    for _ in range(n):
        x, y, z = (random.random() * 2 - 1), (random.random() * 2 - 1), (random.random() * 2 - 1)  # generate point inside cube
        p = np.array([x, y, z])
        p = p / np.linalg.norm(p)
        points.append(p)

    return points


def cylinder(n):
    points = []
    for _ in range(n):
        theta = 2 * math.pi * random.random()
        lvl = random.random()
        if (lvl < 0.2):
            scale = random.random()
            points.append([scale * math.cos(theta), scale * math.sin(theta), -1])
        elif (lvl > 0.8):
            scale = random.random()
            points.append([scale*math.cos(theta), scale*math.sin(theta), 1])
        else:
            points.append([math.cos(theta), math.sin(theta), 2*random.random()-1])
    return points




def square(n):
    pass


if __name__ == "__main__":
    num_shapes = 15
    verts = 500

    header = "OFF\n" + str(verts) + " 0 0\n"
    shapes = [cube, torus, pyramid, sphere, cylinder]
    shape_paths = ["cube/", "torus/", "pyramid/", "sphere/", "cylinder/"]
    base_dir = "../gen_shapes/"

    for i, method in enumerate(shapes):
        for j in range(num_shapes):
            file = open(base_dir + shape_paths[i] + str(j) + ".off", 'w')
            out = header
            points = method(verts)
            for p in points:
                out += "{:f} {:f} {:f}\n".format(p[0], p[1], p[2])
            file.write(out)
            file.close()


