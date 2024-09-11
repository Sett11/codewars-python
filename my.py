def triangle_type(a,b,c):
    a,b,c=sorted([a,b,c])
    x,y=a**2+b**2,c**2
    if not (c<a+b and c>b-a):
        return 0
    return 1 if y<x else 2 if x==y else 3

print(triangle_type(13.999, 692.865, 864.58))
print(triangle_type(317.5, 501.265, 762.758))