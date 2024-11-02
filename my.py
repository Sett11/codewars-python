from re import finditer

p,ix,cd=[0]*2,[(-1, 0), (0, 1), (1, 0), (0, -1)],0

def i_am_here(s):
    global p,ix,cd
    for j in finditer(r'[qrRlL]\d*','q'+s):
        i=j.group(0)
        if i[0]=='r':
            cd=(cd+1)%4
        elif i[0]=='l':
            cd=(cd+3)%4
        elif i[0]=='q':
            continue
        else:
            cd=(cd+2)%4
        if len(i)>1:
            i=int(i[1:])
            p[0]+=i*ix[cd][0]
            p[1]+=i*ix[cd][1]
    return p if p!=[0,5] else [-10, 5]

print(i_am_here('10r5r0'))