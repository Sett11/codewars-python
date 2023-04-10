def fibonacci(n: int) -> int:
    a=[0,1]
    while len(a)<=n:
        a.append(a[len(a)-1]+a[len(a)-2])
    return a[n]

print(fibonacci(34))
