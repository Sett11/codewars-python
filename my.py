from collections import deque

def knight(x,y):
    n,l='12345678','abcdefgh'
    g={i+j:set() for i in l for j in n}
    f=lambda a,b:g[a].add(b)
    for i in range(8):
        for j in range(8):
            v1=l[i]+n[j]
            if 0<=i+2<8 and 0<=j+1<8:
                v2=l[i+2]+n[j+1]
                f(v1,v2)
                f(v2,v1)
            if 0<=i-2<8 and 0<=j+1<8:
                v2=l[i-2]+n[j+1]
                f(v1,v2)
                f(v2,v1)
            if 0<=i+1<8 and 0<=j+2<8:
                v2=l[i+1]+n[j+2]
                f(v1,v2)
                f(v2,v1)
            if 0<=i-1<8 and 0<=j+2<8:
                v2=l[i-1]+n[j+2]
                f(v1,v2)
                f(v2,v1)
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
    r=[y]
    par=p[y]
    while not par is None:
        r.append(par)
        par=p[par]
    return len(r)-1


print(knight('a1','f3'))