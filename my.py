def merge(*a):
    d = list(a)
    o = {}
    for i in d:
        for j in i:
            if (j in o):
                o[j].append(i[j])
            else:
                o[j] = []
                o[j].append(i[j])
    return o


print(merge({"A": 1, "B": 2},{"A": 3}))
