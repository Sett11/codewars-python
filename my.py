from decimal import Decimal as D

def point_in_vector(p,v):
    l=lambda a,b,c,d:round(D(((a-c)**2+(b-d)**2)**.5),5)
    (a,b),(c,d)=v
    x,y=p
    return abs(l(a,b,c,d)-(l(a,b,x,y)+l(c,d,x,y)))<.00001

print(point_in_vector([1,1],[[0, 0], [3, 3]]))
print(point_in_vector([-940.148005310891, -49.545449367196056],[[-940.148005310891, -355.3058135977864], [-940.148005310891, 171.45402379420827]]))