def construct_submatrix(m,r,c):
    q=[list(i) for i in zip(*[j for i,j in enumerate(m) if i not in r])]
    return [list(k) for k in zip(*[j for i,j in enumerate(q) if i not in c])]

print(construct_submatrix([[7, 6, 3, 8, 2, 5],
                           [6, 9, 0, 4, 1, 3],
                           [1, 7, 5, 8, 6, 4],
                           [5, 0, 9, 4, 7, 6],
                           [0, 9, 4, 5, 3, 8]],[3, 4, 2],[2, 4, 3]))