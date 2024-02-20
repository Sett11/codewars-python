def withdraw(n):
    i=0
    while n%50!=0:
        n-=20
        i+=1
    return [(n-50)//100 if n and n%100!=0 else n//100 if n else 0,(1 if n%100!=0 else 0),i]

print(withdraw(260))
print(withdraw(40))