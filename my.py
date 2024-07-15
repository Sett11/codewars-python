def s(x):
    return x+sum(map(int,str(x)))

def f(x):
    u=set()
    for _ in range(20015):
        u.add(x)
        x=s(x)
    return u

a,b,c=f(1),f(3),f(9)

def converging_journeys(n):
    d={1:a,3:b,9:c}
    while 1:
        t=[i for i in d if n in d[i]]
        if t:
            return t[0],n
        n=s(n)
         
print(converging_journeys(108))