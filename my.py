def f(n):
    return all(n%i for i in range(2,int(n**.5+1)))

def is_smooth(n):
    a=[j for j in sum([[i,n//i] for i in range(2,int(n**.5+1)) if n%i==0],[]) if f(j)]
    if not a and not f(n):
        return "non-smooth"
    a=a[-1] if a else n
    return "power of 2" if a==2 else "3-smooth" if a==3 else "Hamming number" if a==5 else "humble number" if a==7 else "non-smooth"


print(is_smooth(111))
print(is_smooth(7))