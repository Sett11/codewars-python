from itertools import groupby as g

def group_ints(a,k):
    q=a.copy()[::-1]
    return [list(j) for _,j in g(a,lambda _:q.pop()<k)]

print(group_ints([1, 1, 1, 0, 0, 6, 10, 5, 10],6))
print(group_ints([-1, -1, -1, 10, 10, 10, -1, -1, -1, 10, -1, 10], 10))