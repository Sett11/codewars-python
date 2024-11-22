def sequence(n):
    return [0, 1, 1, 2, 0, 2, 2, 1][(n-1)%8]

print(sequence(5))