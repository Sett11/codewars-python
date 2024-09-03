def count_squareable(n):
    return len([i for i in range(1,n+1) if i%4!=2])

print(count_squareable(45000))