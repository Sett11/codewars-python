from functools import cache

@cache
def values(n):
    c,k=set(),int(n**.5+1)
    for i in range(1,k):
        t=[i**2]
        for j in range(i+1,k):
            t.append(j**2)
            x=str(sum(t))
            if int(x)>=n:
                break
            if x==x[::-1]:
                c.add(x)
    return len(c)

print(values(1000000))