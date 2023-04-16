def hop_across(a,i=0,j=0,c=0):
    while i<len(a):
        i+=a[i];c+=1
    a.reverse()
    while j<len(a):
        j+=a[j];c+=1
    return c

print(hop_across([2,2,3,1,1,2,1]))