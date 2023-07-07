def possible_positions(p):
    a,b='0abcdefgh',list(p)
    b[0],b[1]=a.index(b[0]),int(b[1])
    return [''.join([a[j[0]],str(j[1])]) for j in sorted([i for i in [[b[0]+2,b[1]+1],[b[0]+1,b[1]+2],[b[0]-2,b[1]-1],[b[0]-1,b[1]-2],[b[0]+1,b[1]-2],[b[0]-2,b[1]+1],[b[0]-1,b[1]+2],[b[0]+2,b[1]-1]] if i[0]>0 and i[1]>0 and i[0]<9 and i[1]<9])]

print(possible_positions('f7'))
print(possible_positions('c3'))