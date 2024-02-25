from itertools import permutations

def sort_bytes(n):
    a=bin(n)[2:].rjust(32,'0')
    return max(int(''.join(i),2) for i in permutations([a[i:i+8] for i in range(0,32,8)]))

print(sort_bytes(1))
print(sort_bytes(3735928559))