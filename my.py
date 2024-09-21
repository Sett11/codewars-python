from collections import deque

def escape(a):
    d={'<':'L','>':'R','^':'U','v':'D'}
    w=''
    r,y=[],[]
    x=0
    for i,k in enumerate(a):
        for j,h in enumerate(k):
            if h==' ':
                r.append((i,j))
                if i==0 or j==0 or i==len(a)-1 or j==len(a[0])-1:
                    y.append((i,j))
            if h in d:
                x=(i,j)
                r.append(x)
                w=h
    if not y:
        return []
    g={i:set() for i in r}
    add=lambda e,c:g[e].add(c) and g[c].add(e)
    for i in g:
        t,k=i
        for j in r:
            p,q=j
            if abs(t-p)<=1 and abs(k-q)<=1 and i!=j and [p,q] not in [[t+1,k+1],[t-1,k-1],[t-1,k+1],[t+1,k-1]]:
                add(i,j)
    dictances={i:None for i in g}
    parents=dictances.copy()
    dictances[x]=0
    q=deque([x])
    while q:
        v=q.popleft()
        for i in g[v]:
            if dictances[i] is None:
                dictances[i]=dictances[v]+1
                parents[i]=v
                q.append(i)
    path=[]
    while y:
        v=y.pop()
        path=[v]
        parent=parents[v]
        while not parent is None:
            path.append(parent)
            parent=parents[parent]
    
    path=path[::-1]
    res=[]
    for i in range(1,len(path)):
        t,b=path[i-1]
        k,n=path[i]
        if t<k:
            if w=='v':
                res.append('F')
                continue
            if w=='^':
                res.append('B')
            if w=='<':
                res.append('L')
            if w=='>':
                res.append('R')
            res.append('F')
            w='v'
        elif t>k:
            if w=='^':
                res.append('F')
                continue
            if w=='v':
                res.append('B')
            if w=='<':
                res.append('R')
            if w=='>':
                res.append('L')
            res.append('F')
            w='^'
        elif b<n:
            if w=='>':
                res.append('F')
                continue
            if w=='<':
                res.append('B')
            if w=='^':
                res.append('R')
            if w=='v':
                res.append('L')
            res.append('F')
            w='>'
        else:
            if w=='<':
                res.append('F')
                continue
            if w=='>':
                res.append('B')
            if w=='^':
                res.append('L')
            if w=='v':
                res.append('R')
            res.append('F')
            w='<'
    return res

print(escape(
['####### #',
 '#>#   # #',
 '#   #   #',
 '#########']))
print(escape(
['# #########',
 '#        >#',
 '###########']))