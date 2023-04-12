def f(x,c=1):
    while x>1:
        c*=x
        x-=1
    return c

def sum_fib(n):
    a=[0,1]
    while len(a)<n:
        a.append(a[len(a)-1]+a[len(a)-2])
    return sum(list(map(f,a)))

print(sum_fib(10))