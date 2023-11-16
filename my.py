def number_of_routes(m,n):
    a=[[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        a[i][0]=1
        for j in range(1,m+1):
            if i==1:
                a[i-1][j]==1
            a[i][j]=a[i-1][j]+a[i][j-1]
    
    return sum(a[-1])

print(number_of_routes(500,600))