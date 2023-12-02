def min_path(a,y,x):
    if [0,0]==[y,x]:
        return a[0][0]
    m,n=x+1,y+1
    r=[[0]*n for _ in range(m)]
    r[0][0]=a[0][0]

    for i in range(m):
        r[i][0]=r[i-1][0]+a[i][0]
    
    for i in range(n):
        r[0][i]=r[0][i-1]+a[0][i]
    
    for i in range(1,m):
        for j in range(1,n):
            r[i][j]=min(r[i-1][j],r[i][j-1])+a[i][j]
    
    return r[x][y]
    
    
print(min_path([
    [1, 2, 3, 6, 2, 8, 1],
    [4, 8, 2, 4, 3, 1, 9],
    [1, 5, 3, 7, 9, 3, 1],
    [4, 9, 2, 1, 6, 9, 5],
    [7, 6, 8, 4, 7, 2, 6],
    [2, 1, 6, 2, 4, 8, 7],
    [8, 4, 3, 9, 2, 5, 8]],4,2))