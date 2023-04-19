def uncensor(s,c):
    c=list(c)
    s=list(s)
    for i in range(len(s)):
        if(s[i]=='*'):
            s[i]=c.pop(0)
    return ''.join(s)

print(uncensor('*h*s *s v*ry *tr*ng*', 'Tiiesae'))