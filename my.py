def mirror(s,c='abcdefghijklmnopqrstuvwxyz'):
    s=list(s.lower())
    for i in range(len(s)):
        s[i]=c[len(c)-c.index(s[i])-1] if s[i] in c else s[i]
    return ''.join(s)

print(mirror("hello", "abcdefgh"))