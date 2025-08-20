a, b, c = "qwertyuiop", "asdfghjkl", "zxcvbnm,."

def z(s, a, n, v):
    if not a:
        return s
    i, l = a.index(s), len(a)
    if v == '+':
        return a[(i + n) % l] if a else s
    while n:
        i -= 1
        if i < 0:
            i = l - 1
        n -= 1
    return a[i]

def f(s, n, dir):
    q = s.isupper()
    x = s.lower()
    v = a if x in a else b if x in b else c if x in c else None
    if dir == '-' and s in '<>':
        v = c
        x = ',' if s == '<' else '.'
        q = True
    k = list(map(int,str(n).rjust(3,'0')))
    w = k[0] if v == a else k[1] if v == b else k[2] if v == c else None
    r = z(x, v, w, dir)
    res = r.upper() if q else r
    if q and res in ',.':
        if res == ',':
            return '<'
        return '>'
    return res

def encrypt(s, n):
    return ''.join(f(i, n, '+') for i in s)
    
def decrypt(s, n):
    return ''.join(f(i, n, '-') for i in s)


print(encrypt("Ball", 134))
print(decrypt('}bdjX tvmo hedpmy', 3))