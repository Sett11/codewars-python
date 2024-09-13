def code(s):
    if not s:
        return ''
    n=len(s)
    k=int(n**.5)
    while True:
        x=k**2
        if x>=n and (x**.5)%1==0:
            break
        k+=1
    s=s.ljust(k**2,chr(11))
    return '\n'.join(''.join(j[::-1]) for j in zip(*[s[i:i+k] for i in range(0,len(s),k)]))

def decode(s):
    if not s:
        return ''
    a=s.split('\n')
    return ''.join([''.join(i).rstrip(chr(11)) for i in zip(*a)][::-1])

print(code("I.was.going.fishing.that.morning.at.ten.o'clock"))
print(decode("""c.nhsoI
ltiahi.
oentinw
cng.nga
k..mg.s
oao.f.
'trtig"""))