import numpy as np
from collections import Counter

def performant_smallest(a,n):
    u,r=Counter(a[i] for i in np.argpartition(a,n)[:n]),[]
    for i in range(len(a)):
        if u[a[i]]:
            r.append(a[i])
            u[a[i]]-=1
    return r

print(performant_smallest([2,1,3,2,3],3))
print(performant_smallest([16, 20, 4, 4, 11, 5, 6, 4, 8, 11, 10, 9, 17, 14, 18, 16, 19, 16, 16, 19, 17, 20, 10, 17, 4, 18, 18, 18, 1, 4, 15, 4, 7, 14, 2, 14, 11, 13, 15, 20, 6, 12, 1, 17, 18, 16, 3, 6, 19, 19, 8, 17, 1, 13, 18, 5, 19, 11, 2, 12, 15, 1, 17, 5, 13, 11, 3, 13, 4, 6, 11, 3, 9, 4, 14, 6, 5, 1, 7, 18, 2, 12, 16, 10, 7, 15, 14, 8, 17, 16, 14, 11, 12, 6, 8, 10, 11, 16, 8, 18],35))