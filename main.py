def f(p, q):
    if p == 0 and q == 0:
        return None
    if p == 1:
        win_first = 1.0
        win_second = 0.0 if q == 1 else 1 - q
        return (win_first, win_second)
    if q == 1:
        win_first = p
        win_second = 0.0
        return (win_first, win_second)
    if p == 0:
        return (0.0, 0.0)
    if q == 0:
        return (1.0, 1.0)
    P1 = p / (1 - (1-p)*(1-q))
    P2 = (1-q)*p / (1 - (1-q)*(1-p))
    return (P1, P2)

print(f(1.0,0.8))