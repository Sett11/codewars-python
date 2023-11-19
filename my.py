def pattern(n):
    a=list(map(str,range(n,0,-1)))
    r=''.join(a)

    for _ in range(n):
        a=a[:-1]
        r+='\n'+''.join(a)

    return r.strip('\n')

print(pattern(11))