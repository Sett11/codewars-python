from itertools import permutations

def permutation_average(n):
    a=[int(''.join(list(i))) for i in permutations(str(n))]
    return round(sum(a)/len(a))

print(permutation_average(737))