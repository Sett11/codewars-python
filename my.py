def finance(n):
    f=lambda k,p:(k+p)*(p-k+1)//2
    p=n
    s=k=0
    while True:
        if k>=p:
            return s+p
        s+=f(k,p)
        k+=2
        p+=1

print(finance(100))