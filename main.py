from string import ascii_lowercase as s

def count_robots(a):
    aut = mec = 0
    def inner_count(e):
        nonlocal aut, mec
        e = e.lower()
        n, x, y, z = len(e), '|};&#[]/><()*', 'automatik' in e, 'mechanik' in e
        if not (y or z):
            return
        for i in range(n - 9):
            if e[i] in s and e[i+1] in x and\
                e[i+2] in x and e[i+3] == '0' and e[i+4] in x and\
                    e[i+5] in x and e[i+6] == '0' and e[i+7] in x and\
                        e[i+8] in x and e[i+9] in s:
                        if y:
                            aut += 1
                        else:
                            mec += 1
    [inner_count(i) for i in a]
    return [f"{aut} robots functioning automatik", f"{mec} robots dancing mechanik"]

print(count_robots(["d[(0)(0)]b We're functioning automatik d[(0)(0)]b","And we are d[(0)(0)]b dancing mechanik d[(0)(0)]b d[(0)(0)]b"]))