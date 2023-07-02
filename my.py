def draw_stairs(n):
    l,a='I',[]
    a.append(l)
    while len(a)<n:
        l=' '+l
        a.append(l)
    return '\n'.join(a)

print(draw_stairs(7))