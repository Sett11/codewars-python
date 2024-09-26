def tv_remote(w):
    symbols={'^': (0, 0), '~': (0, 1), '?': (0, 2), '!': (0, 3), "'": (0, 4), '"': (0, 5), '(': (0, 6), ')': (0, 7), '-': (1, 0), ':': (1, 1), ';': (1, 2), '+': (1, 3), '&': (1, 4), '%': (1, 5), '*': (1, 6), '=': (1, 7), '<': (2, 0), '>': (2, 1), '€': (2, 2), '£': (2, 3), '$': (2, 4), '¥': (2, 5), '¤': (2, 6), '\\': (2, 7), '[': (3, 0), ']': (3, 1), '{': (3, 2), '}': (3, 3), ',': (3, 4), '.': (3, 5), '@': (3, 6), '§': (3, 7), '#': (4, 0), '¿': (4, 1), '¡': (4, 2), '_': (4, 6), '/': (4, 7), 'Aa': (5, 0), ' ': (5, 1)}
    r_l={'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (0, 3), 'e': (0, 4), '1': (0, 5), '2': (0, 6), '3': (0, 7), 'f': (1, 0), 'g': (1, 1), 'h': (1, 2), 'i': (1, 3), 'j': (1, 4), '4': (1, 5), '5': (1, 6), '6': (1, 7), 'k': (2, 0), 'l': (2, 1), 'm': (2, 2), 'n': (2, 3), 'o': (2, 4), '7': (2, 5), '8': (2, 6), '9': (2, 7), 'p': (3, 0), 'q': (3, 1), 'r': (3, 2), 's': (3, 3), 't': (3, 4), '.': (3, 5), '@': (3, 6), '0': (3, 7), 'u': (4, 0), 'v': (4, 1), 'w': (4, 2), 'x': (4, 3), 'y': (4, 4), 'z': (4, 5), '_': (4, 6), '/': (4, 7),'Aa':(5,0),' ':(5,1)}
    r_u={'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 'E': (0, 4), '1': (0, 5), '2': (0, 6), '3': (0, 7), 'F': (1, 0), 'G': (1, 1), 'H': (1, 2), 'I': (1, 3), 'J': (1, 4), '4': (1, 5), '5': (1, 6), '6': (1, 7), 'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4), '7': (2, 5), '8': (2, 6), '9': (2, 7), 'P': (3, 0), 'Q': (3, 1), 'R': (3, 2), 'S': (3, 3), 'T': (3, 4), '.': (3, 5), '@': (3, 6), '0': (3, 7), 'U': (4, 0), 'V': (4, 1), 'W': (4, 2), 'X': (4, 3), 'Y': (4, 4), 'Z': (4, 5), '_': (4, 6), '/': (4, 7), 'Aa': (5, 0), ' ': (5, 1)}
    g,c,curr,k=(0,0),0,[r_l,r_u,symbols],0
    f=lambda x,y:min(abs(x[0]-y[0]),(6-max(x[0],y[0]))%6+min(x[0],y[0]))+min(abs(x[1]-y[1]),(8-max(x[1],y[1]))%8+min(x[1],y[1]))+1
    for i in w:
        if i not in curr[k]:
            x=0
            while i not in curr[k]:
                k=(k+1)%3
                x+=1
            c+=x-1
            q=curr[k]['Aa']
            c+=f(g,q)
            g=q
        t=curr[k][i]
        c+=f(t,g)
        g=t
    return c

print(tv_remote('Too Easy?'),sep='\n')
print(tv_remote("{for}"),sep='\n')
print(tv_remote('^does^'),sep='\n')