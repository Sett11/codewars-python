def f(e):
    e=sum(map(int,str(e)))
    if(len(str(e))==1):
        return e
    return f(e)
def same_encryption(s1,s2):
    s1=s1[0]+str(f(len(s1[slice(1,-1)])))+s1[len(s1)-1]
    s2=s2[0]+str(f(len(s2[slice(1,-1)])))+s2[len(s2)-1]
    return s1==s2

print(same_encryption("fKhjuytrdfcdc","flJc"))