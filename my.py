def pac_man(n,p,en):
    a=[[0]*n for _ in range(n)]
    a[p[0]][p[1]]='p'
    for i,j in en:
        a[i]=['e']*n
        for k in range(n):
            a[k][j]='e'
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=n or isinstance(a[i][j],str):
            return
        if a[i][j]==0:
            a[i][j]='x'
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
    x,y=p
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return sum(a,[]).count('x')

print(*pac_man(6,[4, 1],[[2, 3], [5, 0], [0, 5], [3, 0], [0, 2]]),sep='\n')