def get_matrix(n):
    return [[0 if i!=j else 1 for i,k in enumerate(p)] for j,p in enumerate([[0]*n]*n)]

print(get_matrix(5))