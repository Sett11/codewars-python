def f(x,y):
    while y:
        x.insert(0,x.pop(-1))
        y-=1
    return x

def reorder(a,b):
    return [f(list(range(a//2)),b%(a//2)),f(list(range(a//2,a)),b%(a//2))]

print(reorder(10,97))