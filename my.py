def pin_rook(a,b):
    letters='abcdefgh'
    numbers='12345678'
    chess_board=[[i+j for i in letters] for j in numbers]
    z=[list(i) for i in zip(*chess_board)]
    a,b=a[1:],b[1:]
    r=[i for i in chess_board+z if a in i and b in i]
    if not r:
        return []
    r=r[0]
    g=r.index(b)
    t=r.index(a)
    if g==0 or g==7:
        return []
    if g>t:
        r=r[g+1:]
    else:
        r=r[:g]
    return ['R'+i for i in r]
    

print(pin_rook('Kf5', 'Be5'))