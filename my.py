def evaluate(s):
    a=list(map(int,s.split(' @ ')))

    while len(a)>1:
        b,c=a[0],a[1]
        if not c:
            return
        t=(b+c)+(b-c)+(b*c)+(b//c)
        a[0:2]=[t]
    
    return a[-1]

print(evaluate('1 @ 1 @ -4'))