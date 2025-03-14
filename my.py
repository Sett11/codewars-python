from collections import deque

def can_reach_end(a,n,m,M):
    q,u,ps=deque(),set(),{}
    for i in range(n):
        if a[i][0]<=M:
            q.append((k:=(i,0))),u.add(k)
            ps[k]=None
    while q:
        i,j=q.popleft()
        if j==m-1:
            path=[]
            c=(i,j)
            while c is not None:
                path.insert(0,c)
                c=ps[c]
            return path
        t=[(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1)]
        for x,y in t:
            if 0<=x<n and 0<=y<m and (x,y) not in u and a[x][y]<=M:
                q.append((x,y)),u.add((x,y))
                ps[(x,y)]=(i,j)
    return None

def shallowest_path(a):
    n,m=len(a),len(a[0])
    l,r,p=min(min(i) for i in a),max(max(i) for i in a),None
    while l<=r:
        M=(l+r)//2
        path=can_reach_end(a,n,m,M)
        if path:
            p=path
            r=M-1
        else:
            l=M+1
    return p


print(shallowest_path([
[1, 8, 8],
[8, 1, 8],
[8, 1, 8],
[8, 1, 8],
[8, 1, 8],
[8, 8, 1],
[8, 1, 8],
[8, 1, 1],
[1, 8, 8]]))