def normalize(a,v=None):
    if not a:
        return []
    m=len(max(a,key=len))
    return [i+[v]*(m-len(i)) for i in a]

print(normalize([[1, 4, 2, 6, 7, 2], [3, 1, 4], [8, 9, 4, 4, 0, 9, 8]]))