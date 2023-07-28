from itertools import permutations

def k_permutations_of_n(a,n):
    return [list(i) for i in permutations(a,n)]

print(k_permutations_of_n([1,2,3],2))