def up_down_col_sort(m):
    a=[]
    [a.extend(i) for i in m]
    a=sorted(a)
    i=0
    r=[]
    while i<len(a):
        r.append(a[i:i+len(m)])
        i+=len(m)
    r=[i[1][::-1] if i[0]%2!=0 else i[1] for i in enumerate(r)]
    return [list(i) for i in list(zip(*r))]

print(up_down_col_sort([
    [-20, -4, -1],
     [  1,  4,  7], 
     [  8, 10, 12]]))

#       [[-20, 7, 8],
#       [-4, 4, 10],
#       [-1, 1, 12]]