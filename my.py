def add(a):
    x,r=0,[]
    for i in a:
        x+=i
        r.append(x)
    return r

print(add([1,2,3,4,5]))