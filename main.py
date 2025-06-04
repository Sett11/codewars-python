def calculate_parity(cluster):
    return cluster + [[sum(disk) % 2 for disk in zip(*cluster)]]

def recover_disk(cluster):
    a = cluster.copy()
    b = a.pop()
    if None in b:
        return calculate_parity(a)
    c = [i for i in zip(*a)]
    d = [sum(j for j in i if j is not None) % 2 for i in c]
    for i in range(len(b)):
        if len(set([b[i], d[i]])) != 1:
            c[i] = [1 if j is None else j for j in c[i]]
        else:
            c[i] = [0 if j is None else j for j in c[i]]
    return [list(i) for i in zip(*c)] + [b]

print(calculate_parity([[0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0, 1, 0]]))

print(recover_disk([
  [0,    0, 0, 1],
  [None, 1, 0, 0],
  [1,    1, 0, 1]
]
))