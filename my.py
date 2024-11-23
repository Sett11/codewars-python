from functools import cache

def target_game(a):
    m=float('-inf')
    @cache
    def f(a,t):
        nonlocal m
        if not a:
            m=max(m,t)
            return
        k=a[0]
        if t+k>t:
            f(a[2:],t+k)
        f(a[1:],t)
    f(tuple(a),0)
    return m

print(target_game([11, 82, 47, 48, 80, 35, 73, 99, 86, 32, 32]))