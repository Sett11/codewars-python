from operator import itemgetter

def best_place(a):
    n,m,mosh,r=len(a),len(a[0]),set(),[]

    def f(i,j):
        t=n-i
        if i and a[i-1][j]!=' ':
            t*=.99**(ord(a[i-1][j].lower())-96)
        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=x<n and 0<=y<m and a[x][y].isupper():
                t*=.8
        return t
    
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=m or (i,j) in mosh or a[i][j]!=' ':
            return
        mosh.add((i,j))
        dfs(i+1,j),dfs(i-1,j),dfs(i,j+1),dfs(i,j-1)

    for i in range(n-1):
        for j in range(m-1):
            if (i,j) not in mosh and a[i][j]==' ' and a[i+1][j]==' ' and a[i][j+1]==' ' and a[i+1][j+1]==' ':
                dfs(i,j)
    for i in range(n):
        for j in range(m):
            if a[i][j]==' ':
                r.append(((i,j),f(i,j)))
    q=[i for i in r if i[0] not in mosh]
    if q:
        return max(q,key=itemgetter(1))[0]
    return max(r,key=itemgetter(1))[0]

print(best_place([
            "gbvKq  JfiM I",
            "q jecl   fvoX",
            "L  Foa   ygKT"
        ]))
print(best_place([
            "zzvz",
            "z  z",
            "z  z",
            "zzzz"
        ]))