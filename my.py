def make_2d_list(h,r,c):
    a,r,i,n=[i for i in range(h,r*c+h)],[],0,c
    while i<len(a):
        r.append(a[i:c])
        i+=n
        c+=n
    return r or [[]]

print(make_2d_list(2,3,4))
print(make_2d_list(0,1,0))