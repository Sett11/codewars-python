def is_solved(b):
    a=[]
    [a.extend(i) for i in b]
    return a==sorted(a)

print(is_solved([[0,1],[2,3]]))