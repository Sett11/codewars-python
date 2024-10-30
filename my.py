def max_hexagon_beam(n,a):
    r=[0 for _ in range(6*n-3)]
    z,t=0,3*n-2
    for i in range(2*n-1):
        k=max(i-n+1,0)
        for j in range(i+n-2*k):
            v=a[z%len(a)]
            z+=1
            r[i]+=v
            r[t+k+j-i]+=v
            r[2*t-k-j]+=v
    return max(r)

print(max_hexagon_beam(5,(1,0,4,-10)),sep='\n')
print(max_hexagon_beam(4,(2, 4, 6, 8)),sep='\n')
print(max_hexagon_beam(2,(5,8,3,8)),sep='\n')