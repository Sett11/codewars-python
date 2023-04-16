def rank_of_element(a,i):
    return len(list(filter(lambda e:e<=a[i],a[slice(0,i)])))+len(list(filter(lambda e:e<a[i],a[slice(i+1,len(a))])))

print(rank_of_element([2,1,2,1,2],2))