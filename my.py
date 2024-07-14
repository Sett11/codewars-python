def solve(n,k):
    a=str(n)
    l=len(a)
    c=l-k
    return max(int(a[i:i+c]) for i in range(0,l-c+1))

print(solve('62047312791',3))