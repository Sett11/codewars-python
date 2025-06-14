def simulate(a, n, s, o):
    if n == 0:
        return a
    b, c, l = a.copy(), [s, o], len(a)
    if 0 not in c:
        b[0] = a[1]
    if l - 1 not in c:
        b[-1] = a[-2]
    for i in range(1, l-1):
        if i not in c:
            if a[i-1] == a[i+1]:
                b[i] = a[i-1]
            else:
                t = (a[i-1] + a[i+1]) // 2
                if t != a[i]:
                    b[i] = b[i] + 1 if t > a[i] else b[i] - 1
                else:
                    b[i] = b[i] + 1 if max(a[i-1], a[i+1]) > a[i] else b[i] - 1
    return simulate(b, n-1, s, o) 


print(simulate([0,1,0,2,5,4,8,0,3,4,2], 5, 1, 5))