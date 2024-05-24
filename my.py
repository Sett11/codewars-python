def block_player(x,y):
    a=['x' if i in (x,y) else i for i in range(9)]
    r=[a[i:i+3] for i in range(0,9,3)]
    return [k for k in list(filter(lambda x:x.count('x')==2,r+[list(i) for i in zip(*r)]+[[r[i][i] for i in range(3)]]+[[r[i][2-i] for i in range(3)]]))[0] if k!='x'][0]


print(block_player(6,2))