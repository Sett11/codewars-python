def next_states(s):
    r, a, c = [], [], 0
    if s[-1] == 'I':
        r.append(s + 'U')
    if s[0] == 'M':
        r.append(s + s[1:])
    while (i:=s.find('III', c)) != -1:
        a.append(i)
        c = i + 1
    for i in a:
        t = s[:i]+'U'+s[i+3:]
        if r[-1] != t:
            r.append(t)
    c, a = 0, []
    while (i:=s.find('UU', c)) != -1:
        a.append(i)
        c = i + 1
    for i in a:
        t = s[:i]+''+s[i+2:]
        if r[-1] != t:
            r.append(t)
    return r

print(next_states('MUUUI'))