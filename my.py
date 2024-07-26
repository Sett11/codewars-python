def connected_values(a,v,c):
    n,m,u=len(a),len(a[0]),set()
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=m or (i,j) in u or a[i][j]!=v:
            return
        u.add((i,j))
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j+1)
        dfs(i-1,j-1)
        dfs(i+1,j-1)
        dfs(i-1,j+1)
    dfs(*c)
    return u

print(connected_values([[0, 0, 0, 1, 3, 4, 0, 3],
                [0, 2, 0, 0, 2, 0, 0, 5],
                [0, 0, 0, 2, 0, 1, 1, 1],
                [2, 3, 4, 1, 3, 1, 0, 0],
                [0, 1, 5, 1, 6, 0, 2, 0],
                [2, 0, 2, 3, 1, 1, 1, 1]],0,(0,0)))