def f(x, y):
    r = []
    for i in y:
        if (x % i == 0):
            r.append(i)
    return r


def gangs(d, k):
    l = list(range(1, k+1))
    return len(set(list(map(lambda e: str(f(e, d)), l))))


print(gangs([2, 3, 6, 5], 15))
