def find_nth_occurrence(t,s,n):
    k=0
    while n:
        k=s.find(t,k)
        n-=1
        if k==-1:
            return k
        k+=1
    return k-1

print(find_nth_occurrence('example',"This is an example. Return the nth occurrence of example in this example string.",4))