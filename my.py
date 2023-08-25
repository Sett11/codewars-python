def procedure(n):
    return sum([sum([int(j) for j in list(str(i))]) for i in range(1,101) if not i%n])

print(procedure(30))
print(procedure(25))