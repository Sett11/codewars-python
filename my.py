def spiral_sum(n):
    return n*(n+1)//2+(n//2-(n%2==0))

print(spiral_sum(123456))