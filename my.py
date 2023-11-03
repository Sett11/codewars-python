def crossing_sum(m,r,c):
    return sum(m[r][0:c]+m[r][c+1:]+list(list(zip(*m))[c]))

print(crossing_sum([[1,1,1,1],[2,2,2,2],[3,3,3,3]],1,3))