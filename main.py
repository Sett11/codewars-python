from collections import Counter

def boards_isomorphic(a, b):
    q, w = Counter(a[1::2]), Counter(b[1::2])
    def f(s, p):
        z = [s[i:i+2] for i in range(0, len(s), 2)]
        for i in range(len(z)):
            z[i] = z[i].replace(z[i][1], str(p[z[i][1]]), 1)
        return sorted(z)
    return f(a, q) == f(b, w)


print(boards_isomorphic("4d2d", "2c4c"))
print(boards_isomorphic("4d7dAc", "As4c7s"))