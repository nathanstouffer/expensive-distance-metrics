from random import random
from sys import argv

script, file_name, num_pts = argv
num_pts = int(num_pts)

output = ""

max = 100000

for i in range(0, num_pts):
    x = 2*max*(random()-0.5)
    y = 2*max*(random()-0.5)
    output += str(x) + "," + str(y) + "\n"

fout = open(file_name, 'w')
fout.write(output)
fout.close()
