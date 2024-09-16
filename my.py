def find_height(n):
    if n in [0,1]:
        return n
    i=j=0
    while n>0:
        i+=j
        j+=1
        n-=i
    return j-(1 if n==0 else 2)

print(find_height(7981))
print(find_height(8474))
print(find_height(4))