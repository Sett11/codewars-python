def fusc(n):
    assert type(n)==int and n>=0
    return 0 if n==0 else 1 if n==1 else fusc(n//2) if n%2==0 else fusc(n//2)+fusc(n//2+1)
    
print(fusc(10))