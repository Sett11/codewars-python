def land_perimeter(a):
    n,m,r,s,q,t=len(a),len(a[0]),[],set(),[],0
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=m or (i,j) in s or a[i][j]=='O':
            return
        s.add((i,j))
        r.append((i,j))
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
    for i in range(n):
        for j in range(m):
            if a[i][j]=='X' and (i,j) not in s:
                dfs(i,j)
                q.append(r)
                r=[]
    for l in q:
        if len(l)>1:
            for i,j in l:
                w=sum(1 for x,y in [(h,k) for h,k in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)] if 0<=h<n and 0<=k<m] if a[x][y]=='O')
                t+=w+(1 if i==0 or i==n-1 else 0)+(1 if j==0 or j==m-1 else 0)
        else:
            t+=4
    return f'Total land perimeter: {t}'

print(land_perimeter([
 'OOXOOXXOOX',
 'OXOOOOXXXO',
 'XOXOOXOOOO',
 'OXOXOXXXOO',
 'OOOXXOOXOX',
 'OXOOOOOXOX',
 'OOOOOOXXOO',
 'OOOXOOOOXO',
 'OXXOXXOXXO',
 'OOOXXOOOOX',
 'OXOOXOXXXX',
 'OOXOOXXOXX',
 'XOOOOOOOOO',
 'OOOXOXXXXO',
 'XOXOOOXOOX',
 'OXXOOXXXOX']))