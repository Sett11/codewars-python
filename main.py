def sel_number(n, d):
    c = 0
    for i in range(12, n+1):
        s = str(i)
        if len(set(s)) == len(s) and '0' not in s and ''.join(sorted(s)) == s and max(int(s[j]) - int(s[j-1]) for j in range(1, len(s))) <= d:
            c += 1
    return c

print(sel_number(47, 3))