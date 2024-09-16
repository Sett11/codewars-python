from textwrap import dedent

def cat_mouse(a,n):
    u=set(a)
    if 'C' not in u or 'm' not in u:
        return 'boring without two animals'
    b,c=sum([[[k,i] for i,j in enumerate(p) if j in 'Cm'] for k,p in enumerate(a.splitlines())],[])
    return ('Escaped!','Caught!')[abs(c[0]-b[0])+abs(c[1]-b[1])<=n]
    

print(cat_mouse(dedent("""\
            ..C......
            .........
            ....m...."""),5))