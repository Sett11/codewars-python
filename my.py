import numpy as np

def point_vs_vector(p,v):
    (a,b),(c,d)=v
    x,y=p
    return -np.sign(np.cross([c-a,d-b,0],[x-a,y-b,0])[2])

print(point_vs_vector([0,1],[[0, 0], [1, 1]]))