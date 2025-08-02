def create_triangle(s):
    r = [s]
    while len(r[-1].strip()) > 1:
        w, t = r[-1].split(), []
        for i in range(len(w)-1):
            t.append('+' if w[i] == w[i+1] else '-')
        r.append(' '.join(t).center(len(r[0]), ' '))
    return '\n'.join(r)

print(create_triangle("+ + - + - + +"))