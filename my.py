def display_board(b,w):
    b=[' '+i+' ' for i in b]
    a=[]
    i=0
    while i<len(b):
        a.append(b[i:i+w])
        i+=w
    a=['|'.join(i) for i in a]
    return ('{}'.format('\n'+('-'*len(a[0]))+'\n')).join(a)

print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " "],3))