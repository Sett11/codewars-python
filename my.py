def cinema(b,g):
    if b==g:
        return 'BG'*b
    if b-g==1:
        return 'B'+'GB'*g
    if g-b==1:
        return 'G'+'BG'*b
    if b-g==2 and g>1:
        return ('BG'+'BB'+'GB'*((b-4+g-2) or 1))[:b+g]
    if g-b==2 and b>1:
        return ('GB'+'GG'+'BG'*((g-4+b-2)or 1))[:b+g]

print(cinema(12,14))