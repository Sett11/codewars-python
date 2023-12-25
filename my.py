def min_dot(a,b):
    a,b=sorted(a,reverse=True),sorted(b)
    return sum([a[i]*b[i] for i in range(len(a))])

print(min_dot([1,2,3,4,5],[0,1,1,1,0]))
print(min_dot([1,2,3,4,5], [0,0,1,1,-4]))