from collections import deque

class DynamicConnectivity(object):
    def __init__(self,n):
        self.d={i:set() for i in range(n)}

    def union(self,p,q):
        self.d[p].add(q)
        self.d[q].add(p)
    
    def connected(self,x,y):
        g=self.d
        d={i:None for i in g}
        p=d.copy()
        d[x]=0
        q=deque([x])
        while q:
            v=q.popleft()
            for i in g[v]:
                if d[i] is None:
                    d[i]=d[v]+1
                    p[i]=v
                    q.append(i)
        r=[]
        par=p[y]
        while not par is None:
            r.append(par)
            par=p[par]
        return bool(r[::-1])


results1=DynamicConnectivity(10)

results1.union(4,3)
results1.union(3,8)
results1.union(6,5)
results1.union(9,4)
results1.union(2,1)

print(results1.connected(0,7))
print(results1.connected(8,9))