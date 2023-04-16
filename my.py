def is_inertial(a):
    if(len(a)==0):return False
    l=len(list(filter(lambda e: e%2!=0,a)))
    t=max(a)
    r=list(filter(lambda e: e!=t,a))
    z=list(filter(lambda e: e%2==0,r))
    v=list(filter(lambda e: e%2!=0,r))
    return min(v,default=0)>max(z,default=0) and t%2==0 and l>0

print(is_inertial([11, 4, 20, 9, 2, 8]))