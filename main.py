from functools import lru_cache

@lru_cache(maxsize=None)
def make_sequences(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n//2 + 1):
        result += make_sequences(i)
    return result

print(make_sequences(40))