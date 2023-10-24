def perfect_roots(n):
    r=((n**.5)**.5)**.5
    return r==int(r)

print(perfect_roots(256))