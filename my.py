def tram(n,a,b):
    m=k=0
    for i in range(n):
        k+=b[i]-a[i]
        m=max(m,k)
    return m

print(tram(2, [0, 2, 4, 4], [3, 5, 2, 0]))