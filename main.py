def int_rac(n, x):
    c = 1
    while True:
        y = (x + n // x) // 2
        if abs(x - y) < 1:
            break
        c += 1
        x = y
    return c

print(int_rac(125348,300))