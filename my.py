def rotate_in_place(m):
    a,i=[list(list(i[::-1])) for i in zip(*m)],0
    while i<len(m):
        j=0
        while j<len(m[i]):
            m[i][j]=a[i][j]
            j+=1
        i+=1
    return m

print(rotate_in_place([[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]))