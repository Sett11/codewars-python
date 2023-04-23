def f(x, c=1):
    return c if x == 1 else f(x-1, c*x)


def sum_factorial(l):
    return sum(map(f, l))


print(sum_factorial([4, 6]))
