def binary_pyramid(m,n):
    return bin(sum([int(bin(i)[2:]) for i in list(range(m,n+1))]))[2:]

print(binary_pyramid(1,4))