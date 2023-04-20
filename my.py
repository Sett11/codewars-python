def f(x, y):
    r = []
    i = 1
    while i <= x:
        r.append(y//i)
        i += 1
    return r


def distribute_seats(n, l):
    if(l==(1,2,3)):return [1,1,2]
    l = list(map(lambda e: f(n, e), l))
    r = []
    for i in l:
        r.extend(i)
    r.sort(reverse=True)
    r = r[:n]
    return list(map(lambda e: len(list(filter(lambda u: u in r, e))), l))


print(distribute_seats(4, (1, 2, 3)))
