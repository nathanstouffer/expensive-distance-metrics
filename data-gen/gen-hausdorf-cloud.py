from random import random

dir = '../input/'
filename, clusters, num_pts = "hausdorff-cloud-", 100, 50
filename += str(clusters) + '-' + str(num_pts) + ".in"

max    = 100
radius = 5

output = str(clusters) + ',' + str(num_pts) + '\n'
for c in range(clusters):
    x_center = 2 * max * (random() - 0.5)
    y_center = 2 * max * (random() - 0.5)
    for p in range(num_pts):
        x = 2 * radius * (random() - 0.5) + x_center
        y = 2 * radius * (random() - 0.5) + y_center
        output += str(x) + ',' + str(y) + ';'
    output += '\n'

file = open(dir + filename, 'w')
file.write(output)
file.close()


