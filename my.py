def find_spec_partition(n,k,c):
    if c=='min':
        return [n-(k-1)]+[1]*(k-1)
    a,i=[n//k]*k,0
    while sum(a)<n:
        a[i]+=1
        i+=1
    return a
    

print(find_spec_partition(10,4,'max'))
print(find_spec_partition(13,6,'max'))
print(find_spec_partition(10,4,'min'))