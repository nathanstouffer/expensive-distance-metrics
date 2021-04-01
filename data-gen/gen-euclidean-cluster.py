import numpy as np
from random import random
from sys import argv

script, file_name, num_clusters, num_pts = argv
num_clusters = int(num_clusters)
num_pts      = int(num_pts)

output = str(num_pts) + "\n"

max    = 300
radius = 10

num_noise   = int(0.05*num_pts)
rem         = num_pts-num_noise
pts_cluster = int(rem/num_clusters)

centers = []

for i in range(0, num_clusters):
    x = 2 * max * (random() - 0.5)
    y = 2 * max * (random() - 0.5)
    centers.append(np.array([x, y]))

counter = 0
for i in range(0, num_clusters):
    for j in range(0, pts_cluster):
        x = centers[i][0]+2*radius*(random()-0.5)
        y = centers[i][1]+2*radius*(random()-0.5)
        output += str(x) + "," + str(y) + "\n"
        counter += 1

for i in range(counter, num_pts):
    x = 2 * max * (random() - 0.5)
    y = 2 * max * (random() - 0.5)
    output += str(x) + "," + str(y) + "\n"
    counter += 1

fout = open(file_name, 'w')
fout.write(output)
fout.close()
