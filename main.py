from string import ascii_uppercase as a, digits as d
from collections import Counter

def convert(n, b, w=1):
    r, s = (d + a)[:b], ''
    while n > 0:
        s = r[n%b] + s
        n //= b
    return s.rjust(w, '0')

def validate(b, w, a):
    s = ''.join(convert(i, b, w) for i in a)
    c = Counter(s)
    for i in range(len(a)):
        if c[convert(i, b)] != a[i]:
            return False
    return True

print(validate(16,2,[0x1B, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00]))