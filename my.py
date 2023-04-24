def f(x,y):
    i=len(x)-1
    c=0
    t=0
    while i>=0:
        q=int(x[i])+int(y[i])
        if(q+t>9):
            t=1
        if(q+t<10):
            t=0
        if(q+t>9):
            c+=1
            t=1
        i-=1
    return c

def solve(s):
    s=s.split()
    i=0
    r=[]
    while i<len(s):
        r.append(f(s[i],s[i+1]))
        i+=2
    return '\n'.join(map(lambda e: 'No carry operation' if not e else '{} carry operations'.format(e),r))

print(solve("321 679\n098 805\n123 867"))