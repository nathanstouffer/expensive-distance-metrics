import metrics

def function(x):
    return x ** 3

def dist1(p1,p2):
    return 3

def dist2(p1, p2):
    return 4


p1 = (0,0,0)
p2 = (1,1,1)
print(metrics.euclidean(p1,p2))
