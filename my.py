def solve(n):
    for i in range(int(n**.5),0,-1):
        k=n-i**2
        if k>0 and k%(2*i)==0:
            return (k//(2*i))**2
    return -1

print(solve(17))
print(solve(3))
print(solve(9))
print(solve(88901))