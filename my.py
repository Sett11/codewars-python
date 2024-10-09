from collections import Counter
from sys import setrecursionlimit

setrecursionlimit(40000)

def components(grid):
    a=[list(i) for i in grid.replace(' ','&').replace('+&&','+  ').splitlines()]
    n,m,u,r=len(a),len(a[0]),set(),[]
    for i in range(1,n-1):
        for j in range(m):
            if a[i][j]=='&' and a[i-1][j]=='+' and a[i+1][j]=='+':
                a[i][j]=' '
    a=[''.join(i).replace('&&','& ') for i in a]
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=m or (i,j) in u or a[i][j] not in '& ':
            return
        u.add((i,j))
        if a[i][j]=='&':
            r[-1].append((i,j))
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    for i in range(n):
        for j in range(m):
            if a[i][j]=='&' and (i,j) not in u:
                r.append([])
                dfs(i,j)
    return sorted(Counter([len(i) for i in r]).items(),reverse=True)

print(components('''\
+--+--+--+
|  |     |
+  +  +--+
|  |  |  |
+--+--+--+'''),sep='\n')
print(components('''\
+--+--+--+
|  |  |  |
+--+--+--+
|  |  |  |
+--+--+--+'''),sep='\n')
print(components('''\
+--+--+--+--+--+--+--+--+--+--+
|  |           |  |  |        |
+--+  +--+--+--+--+--+--+--+--+
|  |           |     |  |  |  |
+  +--+--+--+  +  +--+--+--+--+
|     |  |  |  |  |  |     |  |
+--+--+  +--+  +  +--+--+  +--+
|     |  |  |           |     |
+--+--+--+--+--+--+--+--+  +--+
|           |        |  |  |  |
+  +--+  +  +--+--+--+  +--+--+
|  |     |  |     |  |  |  |  |
+--+  +--+--+  +--+  +--+--+  +
|  |     |     |  |  |  |  |  |
+  +  +--+--+--+--+--+--+--+  +
|  |  |  |  |  |     |  |  |  |
+--+  +  +  +  +--+--+--+--+--+
|  |  |  |  |  |        |  |  |
+--+--+  +  +--+--+  +--+--+--+
|        |        |  |  |     |
+--+--+--+--+--+--+--+--+--+--+'''),sep='\n')