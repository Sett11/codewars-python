def get_candy_position(n,c,r,k):
    a,y=list(range(1,n+1)),1
    while a:
        t=[[0]*r for _ in range(c)]
        q=a[:r*c]
        a=a[r*c:]
        x=0
        for i in range(c-1,-1,-1):
            for j in range(r-1,-1,-1):
                if x>=len(q):
                    return [-1]*3
                if q[x]==k:
                    return [y,i,j]
                t[i][j]=q[x]
                x+=1
        y+=1
    return [-1]*3


print(get_candy_position(15,3,3,14))
print(get_candy_position(8,4,2,3))