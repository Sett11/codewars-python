import numpy as np

def point_vs_vector_v2(p,v):
    if v==[[0.]*2]*2:
        return None
    (a,b),(c,d)=v
    x,y=p
    z=np.cross([c-a,d-b,0],[x-a,y-b,0])[2]
    if abs(z)<1e-9:
        z=0
    return -np.sign(z)

print(point_vs_vector_v2([0,1],[[0, 0], [1, 1]]))