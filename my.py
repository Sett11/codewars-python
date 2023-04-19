def max_sum_between_two_negatives(a):
    i=0
    j=0
    m=0
    while i<len(a):
        if(a[i]<0):
            j=i+1
            while j<len(a):
                if(a[j]<0):
                    m=max(sum(a[i+1:j]),m)
                    break
                j+=1
        i+=1
    return m if len(list(filter(lambda e:e<0,a)))>1 else -1

print(max_sum_between_two_negatives([1,-2]))