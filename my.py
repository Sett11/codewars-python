def solve(n,k):
    c,r,t=2,[1],[1]
    while c<=k:
        r+=t+(([c] if c!=k else [])+(t[::-1] if c!=k else []))
        t+=[c]
        c+=1
    return sum(r[::n][1:])

print(solve(2,4))
print(solve(3,3))