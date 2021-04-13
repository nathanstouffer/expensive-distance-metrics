import numpy as np
from random import random
from sys import argv



dir = '../input/'

# script, file_name, num_clusters, num_pts = argv
file_name, big_clusters, total_num_clusters, pts_cluster = "hausdorff-cloud-cluster-4-100-20.in", 4, 100, 20
total_num_clusters = int(total_num_clusters)

output = str(total_num_clusters) + ',' + str(pts_cluster) + "\n"

max    = 100
radius = 5

num_noise   = int(0.05 * total_num_clusters)
rem         = total_num_clusters - num_noise
clusters_per_cluster = int(rem / big_clusters)

centers = []


def make_cluster(num_pts):
    center_x = 2 * max * (random() - 0.5)
    center_y = 2 * max * (random() - 0.5)
    p = []
    for _ in range(num_pts):
        x = center_x + 2 * radius * (random() - 0.5)
        y = center_y + 2 * radius * (random() - 0.5)
        p.append([x,y])
    return p


for _ in range(big_clusters):
    clust = make_cluster(clusters_per_cluster)
    for c in clust:
        centers.append(np.array(c))
        for _ in range(pts_cluster):
            x = c[0] + 2 * radius * (random() - 0.5)
            y = c[1] + 2 * radius * (random() - 0.5)
            output += str(x) + ',' + str(y) + ';'
        output += '\n'

for _ in range(num_noise):
    c = make_cluster(pts_cluster)
    for p in c:
        output += str(p[0]) + ',' + str(p[1]) + ';'

fout = open(dir + file_name, 'w')
fout.write(output)
fout.close()
