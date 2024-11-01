def how_many_step(a,b,c=0):
    return c if a==b else c+(b-a) if b//2<a else how_many_step(a,b//2 if b%2==0 else b-1,c+1)

print(how_many_step(1,17))
print(how_many_step(644, 4622))
print(how_many_step(709, 1102))
print(how_many_step(28, 2957))
print(how_many_step(197, 2640))