def shortest_steps_to_num(n):
    c=0
    while n!=1:
        if(n&1):
            n-=1
            c+=1
        else:
            n//=2
            c+=1
    return c

print(shortest_steps_to_num(71))