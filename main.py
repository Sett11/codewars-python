def super_pad(s, n, f=" "):
    if not n:
        return ''
    if not f:
        return s[-n:]
    if  f[0] not in '<>^':
        a, b, r, i = list(s), list(f), [], 0
        while len(r+a) < n:
            r.append(b[i%len(b)])
            i += 1
        return ''.join(r+a)[-n:]
    if f[0] == '<':
        a, b, r, i = list(s), list(f[1:]), [], 0
        while len(r+a) < n:
            r.append(b[i%len(b)])
            i += 1
        return ''.join(r+a)[-n:]
    if f[0] == '>':
        return (s+f[1:]*n)[:n]
    a, b, c, r = list(s), list(f[1:]), list(f[1:]), []
    if not b:
        return s[-n:]
    i = j = 0
    while len(r+a) < n:
        r.append(b[i%len(b)])
        if len(r+a) < n:
            a.append(c[j%len(c)])
        i+=1
        j+=1
    return ''.join(r+a)

print(super_pad("test", 7, "^more complex"))