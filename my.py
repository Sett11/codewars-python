a=sorted(filter(lambda n:n>=2 and all(n%i for i in range(2,int(n**.5+1))),[2**i*3**j+1 for i in range(25) for j in range(11)]))

def solve(x,y):
    return len([i for i in a if x<=i<=y])

print(solve(0,1500000))