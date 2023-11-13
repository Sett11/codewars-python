def square(n):
    c=[1]
    for _ in range(1,n):
        c.append(c[-1]*2)
    return c[-1]

print(square(32))