def partitions(n):
    d=[1]+[0]*n
    for i in range(1,n+1):
        for j in range(i,n+1):
            d[j]+=d[j-i]
    return d[-1]

print(partitions(5))