import numpy as np
from itertools import cycle

def f(a):
    r,d1,d2,d3,d4=[],[],[],[],[]
    for i in range(4):
        r.extend([list(np.diag(a[i])),list(np.diag([j[::-1] for j in a[i]]))])
        r.extend(sum([[list(j) for j in a[i].T]],[]))
        r.extend([list(j) for j in a[i]])
        r.extend([list(j) for j in np.transpose(a[i].T,(1,0))])
        d1.append(a[i,i,i])
        d2.append(a[-i-1,-i-1,-i-1])
        d3.append(a[i,-i-1,i])
        d4.append(a[i,-i-1,-i-1])
    return r+[d1,d2,d3,d4]

def check(a):
    w=f(a)+f((t:=a.T))+f(np.transpose(t,(1,0,2)))
    for i in w:
        if len(set(i))==1 and i[0]:
            return i[0]

def play_OX_3D(moves):
    a,w,c=np.zeros(shape=(4,4,4)),{1:'O',2:'X'},cycle([1,2])
    for i in range(len(moves)):
        a[*moves[i]]=next(c)
        if i>3:
            v=check(a)
            if v:
                return f'{w[int(v)]} wins after {i+1} moves'
    return 'No winner'

print(play_OX_3D([[0, 2, 3], [0, 1, 2], [0, 0, 0], [2, 2, 3], [1, 1, 1], [2, 0, 2], [0, 1, 3], [1, 3, 3], [2, 1, 2], [2, 2, 2], [1, 2, 3], [2, 0, 3], [1, 0, 2], [2, 1, 0], [2, 3, 2], [0, 2, 1], [3, 0, 3], [2, 3, 0], [2, 0, 1], [0, 0, 1], [0, 3, 0], [2, 1, 1], [0, 2, 2], [1, 1, 2], [1, 2, 1], [3, 0, 0], [2, 3, 3], [1, 3, 1], [0, 0, 2], [3, 0, 1], [0, 0, 3], [1, 3, 0], [1, 0, 1], [3, 1, 1], [3, 0, 2], [1, 2, 2], [2, 2, 1], [2, 3, 1], [1, 2, 0], [0, 3, 3], [0, 3, 2], [1, 0, 3], [2, 0, 0], [0, 1, 1], [1, 1, 0], [3, 1, 0], [0, 2, 0], [0, 3, 1], [0, 1, 0], [2, 1, 3], [1, 0, 0], [2, 2, 0], [1, 1, 3], [1, 3, 2]]))