def sequence(x):
    return [int(j) for j in sorted(str(i) for i in range(1,x+1))]

print(sequence(66))