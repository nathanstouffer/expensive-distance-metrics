# python file which contains functions that select the next edge for
# the approximation algorithm

import numpy as np
import random
from random import randint


def blind_random(lower, upper, eps):
    n = len(lower)  # get the number of elements we are considering
    start_i = randint(0, n - 1)  # start at a random point in the (symmetric) bound matrices
    start_j = randint(0, n - 1)

    for i in range(n + 1):
        for j in range(n):
            x = (i + start_i) % n
            y = (j + start_j) % n
            if above(lower, upper, x, y, eps):
                return np.array([x, y])
    return np.array([-1,-1])



# function to return the pair (i,j) that maximizes the ratio upper_{ij}/lower_{ij}
def blind_greedy(lower, upper, eps):
    n = len(lower)  # get the number of elements we are considering
    max = 0
    max_indx = np.array([-1, -1])
    for i in range(n):
        for j in range(i+1, n):
            u = upper[i][j]
            l = lower[i][j]
            if (l == 0.0):
                return np.array([i,j])
            if (u/l > 1+eps):
                if (u/l > max):
                    max = u/l
                    max_indx = np.array([i, j])
    return max_indx


def above(lower, upper, i, j, eps):
    if (i == j):
        return False
    if (lower[i][j] == 0.0):
        return True
    return upper[i][j]/lower[i][j] > 1+eps