def tv_remote(w):
    r={'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (0, 3), 'e': (0, 4), '1': (0, 5), '2': (0, 6), '3': (0, 7), 'f': (1, 0), 'g': (1, 1), 'h': (1, 2), 'i': (1, 3), 'j': (1, 4), '4': (1, 5), '5': (1, 6), '6': (1, 7), 'k': (2, 0), 'l': (2, 1), 'm': (2, 2), 'n': (2, 3), 'o': (2, 4), '7': (2, 5), '8': (2, 6), '9': (2, 7), 'p': (3, 0), 'q': (3, 1), 'r': (3, 2), 's': (3, 3), 't': (3, 4), '.': (3, 5), '@': (3, 6), '0': (3, 7), 'u': (4, 0), 'v': (4, 1), 'w': (4, 2), 'x': (4, 3), 'y': (4, 4), 'z': (4, 5), '_': (4, 6), '/': (4, 7),'Aa':(5,0),' ':(5,1)}
    g,c,v=(0,0),0,False
    f=lambda x,y:min(abs(x[0]-y[0]),(6-max(x[0],y[0]))%6+min(x[0],y[0]))+min(abs(x[1]-y[1]),(8-max(x[1],y[1]))%8+min(x[1],y[1]))+1
    for i in w:
        if i.isupper() and not v:
            v=True
            q=r['Aa']
            c+=f(g,q)
            g=q
        if i.islower() and v:
            v=False
            q=r['Aa']
            c+=f(g,q)
            g=q
        t=r[i.lower()]
        c+=f(t,g)
        g=t
    return c

print(tv_remote('FOR'))
print(tv_remote('Code Wars'))
print(tv_remote('Solution'))
print(tv_remote('Does'))