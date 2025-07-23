from itertools import combinations as c

def k_bits_digits(n, k):
    if k == 0:
        return [0]
    if n < k:
        return []
    if n == k:
        return [(1 << n) - 1]
    a = []
    for bits in c(range(n), k):
        t = 0
        for bit in bits:
            t |= (1 << (n - 1 - bit))
        a.append(t)
    return sorted(a)


print(k_bits_digits(5, 3))