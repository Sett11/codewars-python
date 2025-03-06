def check_course(a):
    a=list(map(list,a))
    n,m=len(a),len(a[0])
    x=y=0
    for i in range(n):
        if a[i][0]=='X':
            x=i
            break
    f=lambda x,y:'N' in [a[i][j] for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)] if 0<=i<n and 0<=j<m]
    u,d=[[0,i] for i in range(m) if a[0][i]=='N'],[[n-1,i] for i in range(m) if a[n-1][i]=='N']
    for _ in range(m):
        if f(x,y):
            return False
        a[x][y]='0'
        y+=1
        a[x][y]='X'
        if u and u[0][0]==n-1:
            u,d=d,u
        elif d and d[0][0]==0:
            u,d=d,u
        for i in range(len(u)):
            a[u[i][0]][u[i][1]]='0'
            u[i][0]+=1
            a[u[i][0]][u[i][1]]='N'
        for i in range(len(d)):
            a[d[i][0]][d[i][1]]='0'
            d[i][0]-=1
            a[d[i][0]][d[i][1]]='N'
        if y==m-1 and not f(x,y):
            return True
    return True
        


print(check_course([ '000000',
                '000000',
                'X00000',
                '000000',
                '00N000']),sep='\n')