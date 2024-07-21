def jump_to(n):
    n=abs(n)
    k=i=0
    while i<n or (i-n)%2:
        k+=1
        i+=k
    return k
    
print(jump_to(6))
print(jump_to(7))
print(jump_to(100))