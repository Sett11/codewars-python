def monkey_count(n):
    c=1
    a=[]
    while c<=n:
        a.append(c)
        c+=1
    return a

print(monkey_count(11))