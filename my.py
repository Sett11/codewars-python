def fraction(a,b):
    i=2
    while i<=a or i<=b:
        while a%i==0 and b%i==0:
            a//=i
            b//=i
        i+=1
    return a+b

print(fraction(3,118))
print(fraction(5,5))