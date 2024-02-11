def diagonal_sort(a):
    n,m=len(a),len(a[0])
    r,a=[[0]*m for _ in range(n)],sum(a,[])[::-1]
    for i in range(n+m-1):
        k,j=i if i<n else n-1,0 if i<n else i-n+1
        while k>=0 and j<m:
            r[k][j]=a.pop()
            k-=1
            j+=1
    return r

print(diagonal_sort([['c','o','d'],
              ['i','n','g']]))