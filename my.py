x,y=0,1

def gcdExtended(a, b):
    global x,y
    if a==0:
        x,y=0,1
        return b
    g=gcdExtended(b%a,a)
    x1,y1=x,y
    x,y=y1-(b//a)*x1,x1
    return g


def inverse_mod(a,m):
    g=gcdExtended(a,m)
    if g==1:
        return (x%m+m)%m

print(inverse_mod(101014,125445))
print(inverse_mod(48,101))