def off(n):
    n+=1
    a,j=[False]*(n),1
    while n:
        for i in range(0,len(a),j):
            a[i]=not a[i]
        j+=1
        n-=1
    return [i+1 for i,j in enumerate(a[1:]) if j]


print(off(9))