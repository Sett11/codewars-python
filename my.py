def damaged_or_sunk(b,a):
    q,w,r,o=b.copy(),sum([[b[k][i] for i,j in enumerate(h) if j] for k,h in enumerate(b)],[]),[],{ 'sunk': 0, 'damaged': 0 , 'not_touched': 0, 'points': 0 }
    s=set(w)
    for i in range(len(a)):
        q[len(q)-a[i][1]][a[i][0]-1]='&'
    q=[i for i in sum(q,[]) if i and i!='&']
    for i in s:
        r.append([w.count(i),q.count(i)])
    for i in r:
        if not i[1]:
            o['sunk']+=1
            o['points']+=1
        if i[1] and i[1]!=i[0]:
            o['damaged']+=1
            o['points']+=.5
        if i[0]==i[1]:
            o['not_touched']+=1
            o['points']-=1
    return o

print(damaged_or_sunk([
         [0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]],[[2, 1], [1, 3], [4, 2]]))

print(damaged_or_sunk([ [3, 0, 1],
          [3, 0, 1],
          [0, 2, 1], 
          [0, 2, 0] ],[[2, 1], [2, 2], [ 3, 2], [3, 3]]))