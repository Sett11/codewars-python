def climbing_stairs(a):
    n=len(a)
    r=a[:2]+[0]*(n-2)
    for i in range(2,n):
        r[i]=min(r[i-1],r[i-2])+a[i]
    return min(r[-1],r[-2])

print(climbing_stairs([0, 2, 3, 2]))
print(climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(climbing_stairs([10,15,20]))