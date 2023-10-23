def sum_and_multiply(s,m):
    if not s or not m:
        return sorted([s,m])
    a=[i for i in range(s)]
    for i in range(len(a)):
        t=s-a[i]
        if t in a and t*a[i]==m:
            return sorted([a[i],t])


print(sum_and_multiply(12,32))