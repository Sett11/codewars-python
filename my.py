number_increasing=f=lambda n:1==2 if n<1 else n%5==1 or f(n-5 if n%3 else n//3)
    

print(number_increasing(54321))