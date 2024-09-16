def vector_length(a):
    a,b=a
    return ((b[0]-a[0])**2+(b[1]-a[1])**2)**.5

print(vector_length([[0, 3],[4, 0]]))