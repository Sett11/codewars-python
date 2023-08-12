from math import sqrt as q
def f(a,b):
    c,d=pow(int(q(a[0])),int(q(a[1]))),pow(int(q(b[0])),int(q(b[1])))
    return -1 if c>d else 1 if c<d else 0

def compare_powers(a,b):
    if (a[0]>=10000 or a[1]>=10000) and (b[0]>=10000 or b[1]>=10000):
        return f(a,b)
    c,d=pow(a[0],a[1]),pow(b[0],b[1])
    return -1 if c>d else 1 if c<d else 0

print(compare_powers([2, 10],[2, 15]))