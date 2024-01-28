def to_and_from(x,y,t):
    a,b=divmod(t,abs(y-x))
    return y-b if x<y and a&1 else y+b if a&1 else x-b if t<x-y else x-b if x>y else x+b

print(to_and_from(42,150,548))
print(to_and_from(10,4,8))
print(to_and_from(1,10,8))
print(to_and_from(96,14,74))
print(to_and_from(94,65,77))