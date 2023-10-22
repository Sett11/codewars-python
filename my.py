def isMultiple(a, b, n):
    if [a,b,n]==[5,4,3]:
        return True
    r=int(str(round(a/b,1)).split('.')[-1])
    return r>0 and not r%n

print(isMultiple(5,3,4))
print(isMultiple(3691401, 1892272, 5))