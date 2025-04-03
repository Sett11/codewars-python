import heapq
from collections import deque

def f(a,b):
    q,w=a
    x,y=b
    return 'down' if x<q else 'up' if x>q else 'right' if y<w else 'left'

def cheapest_path(a,s,e):
    if s==e:
        return []
    n,m,h,r,u=len(a),len(a[0]),[(a[s[0]][s[1]],s)],{s:None},set()
    while h:
        v,(i,j)=heapq.heappop(h)
        if (i,j) in u:
            continue
        u.add((i,j))
        if (i,j)==e:
            c,q=(i,j),deque()
            while c is not None:
                nc=r[c]
                if nc:
                    q.appendleft(f(c,nc))
                c=nc
            return list(q)
        for x,y in [(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<n and 0<=y<m]:
            if (x,y) not in r or (r[(x,y)] is not None and v+a[x][y]<a[r[(x,y)][0]][r[(x,y)][1]]):
                r[(x,y)]=(i,j)
            heapq.heappush(h,(v+a[x][y],(x,y)))


print(cheapest_path([[1,9,1],[2,9,1],[2,1,1]],(0,0),(0,2)))
print(cheapest_path([[1, 19, 1, 1, 1],
                     [1, 19, 1, 19, 1],
                     [1, 19, 1, 19, 1],
                     [1, 19, 1, 19, 1],
                     [1, 1, 1, 19, 1]], (0, 0), (4, 4)))