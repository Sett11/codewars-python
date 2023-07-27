import math

def approx_root(n):
    q=math.sqrt(n)
    c=math.floor(q)
    a,b=c**2,math.ceil(q)**2
    d1,d2=n-a,b-a
    return int(q) if int(q)==q else round(c+(d1/d2),2)

print(approx_root(213))
print(approx_root(400))
print(approx_root(2))