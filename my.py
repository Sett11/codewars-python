def solve(a,b):
    m,n=len(a),len(b)
    r=[0]*m
    for i in range(n):
        for j in range(m-1,-1,-1):
            if b[i]==a[j]:
                r[j]+=r[j-1] if j else 1
    return r[-1]

print(solve("zaz","zazapulz"))