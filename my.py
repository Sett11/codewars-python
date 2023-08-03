def grid(n):
    s,i,a='abcdefghijklmnopqrstuvwxyz',0,[]
    while i<n:
        a.append([j for j in range(i,i+n)])
        i+=1
    return '\n'.join([' '.join([s[i%len(s)] for i in j]) for j in a]) if n>-1 else None

print(grid(2))