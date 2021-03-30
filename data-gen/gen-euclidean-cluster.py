import numpy as np
from random import random
from sys import argv

script, file_name, num_clusters, num_pts = argv
num_clusters = int(num_clusters)
num_pts      = int(num_pts)

output = str(num_pts) + "\n"

max = 100000

centers = []

for i in range(0, num_clusters):
    x = 2 * max * (random() - 0.5)
    y = 2 * max * (random() - 0.5)
    centers.append(np.array([x, y]))
    output += str(x) + "," + str(y) + "\n"



for i in range(0, num_pts-num_clusters):
    x = 2*max*(random()-0.5)
    y = 2*max*(random()-0.5)
    output += str(x) + "," + str(y) + "\n"

fout = open(file_name, 'w')
fout.write(output)
fout.close()
