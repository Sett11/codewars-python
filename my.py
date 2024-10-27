def all_alone(a):
    n,m,u,v=len(a),len(a[0]),set(),True
    def dfs(i,j):
        nonlocal v
        if not v or i<0 or i>=n or j<0 or j>=m or (i,j) in u or a[i][j] not in 'Xo ':
            return
        if a[i][j]=='o':
            v=False
            return
        u.add((i,j))
        dfs(i+1,j),dfs(i-1,j),dfs(i,j+1),dfs(i,j-1)
    for i in range(n):
        for j in range(m):
            if a[i][j]=='X':
                dfs(i,j)
    return v

print(all_alone([
            list("  o                o        #######"),
            list("###############             #     #"),
            list("#             #        o    #     #"),
            list("#  X          ###############     #"),
            list("#                                 #"),
            list("###################################")
        ]))