def gen(k,it):
    w,g,i=[],iter(it),0
    for _ in range(2000):
        try:
            w.append(next(g))
        except:
            break
    w*=200
    while 'fack':
        yield tuple(w[i:i+k])
        i+=1

g=gen(2,range(7))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))