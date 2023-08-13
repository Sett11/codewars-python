def pattern(n):
    a,r=[i for i in range(1,n+1)],[]
    for i in range(n):
        r.append(''.join([str(j) for j in a[i:]+a[:i]]))
    return '\n'.join(r)

print(pattern(9))