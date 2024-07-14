def solve(s,k):
    a=s.split()
    c,n=0,len(a)
    for i in range(n):
        for j in range(i+1,n):
            if int(a[i]+a[j])%k==0:
                c+=1
            if int(a[j]+a[i])%k==0:
                c+=1
    return c

print(solve('1 2 36 4 8',2))