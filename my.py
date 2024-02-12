def f(x):
    a=set([x])
    for i in range(2,int(x**.5+1)):
        if x%i==0:
            a.update([i,x//i])
    return sorted(a,reverse=True)

def check(a):
    return all(i**.5!=int(i**.5) for i in a)

def square_free_part(n):
    a=f(n)
    if check(a):
        return n
    for i in a:
        if check(f(i)):
            return i


print(square_free_part(2499))