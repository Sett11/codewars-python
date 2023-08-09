def skiponacci(n):
    a=b,c,r,v=0,1,[],True
    while len(r)<n:
        a=b+c
        c=b
        b=a
        r.append(str(a) if v else 'skip')
        v=not v
    return ' '.join(r)

print(skiponacci(21))