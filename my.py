def promotion(l):
    if('P' not in l[7]):
        return []
    v=0
    for i in l:
        if('K' in i):
            v=1
    if(not v):
        return []
    a,b=0,0
    c,d=0,0
    for i,j in enumerate(l):
        for x,y in enumerate(j):
            if(y=='K'):
                a,b=i,x
            if(y=='P'):
                c,d=i,x
    r=[[a,b],[c,d]]
    rr=[]
    if(r[0][0]==r[1][0] or r[0][1]==r[1][1]):
        rr.append('queen')
        rr.append('rook')
    if(r[1][0]-r[0][0]==1 and abs(r[1][1]-r[0][1])==2 or r[1][0]-r[0][0]==2 and abs(r[1][1]-r[0][1])==1):
        rr.append('knight')
    if(abs(r[1][0]-r[0][0])==abs(r[1][1]-r[0][1])):
        rr.append('queen')
        rr.append('bishop')
    return rr

print(promotion([
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ']]))