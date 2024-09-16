cubes=set([i**3 for i in range(1000)])

def you_are_a_cube(n):
    return n in cubes

print(you_are_a_cube(125000000))