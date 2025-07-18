def barista(a):
    if not a:
        return 0
    a.sort()
    r = [a[0]]
    for i in a[1:]:
        r.append(r[-1] + 2 + i)
    return sum(r)

print(barista([4,3,2]))
print(barista([2,10,5,3,9]))