from itertools import product

def furthest_distance(a):
    return max(map(lambda x:round(((x[1][0]-x[0][0])**2+(x[0][1]-x[1][1])**2)**.5,2),product(a,repeat=2)))