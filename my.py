def is_madhav_array(a):
    if len(a)<2:
        return False
    i,r=1,[]
    while a:
        t=a[0:i]
        if len(t)!=i:
            return False
        r.append(sum(t))
        a=a[i:]
        i+=1
    return len(set(r))==1


print(is_madhav_array([6,2,4,2,2,2,1,5,0,0]))