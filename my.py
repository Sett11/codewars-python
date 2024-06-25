from functools import lru_cache

@lru_cache(None)
def lcs(x, y):
    if not (x and y): return ''
    if x[0] == y[0]: return x[0] + lcs(x[1:], y[1:])
    return max(lcs(x, y[1:]), lcs(x[1:], y), key=len)


print(lcs("abcdefghijklmnopq", "apcdefghijklmnobq"))