from re import sub

def find_longest_substr(s):
    a,m,d,t=sub(r'(.)\1*',lambda x:' '+x.group()[0]+str(len(x.group()))+' ',s).split(),1,{},0
    for i in a:
        x=int(i[1:])
        if i[0].isdigit() or i[0].isalpha():
            if x>m:
                d[x]=[str(ord(i[0])),x,[t,t+x-1]]
                m=x
        t+=x
    return d[m]
    

print(find_longest_substr("1111aa994bbbb1111AAAAAFF????????????????????????????"))
print(find_longest_substr("1111aa994bbbb1111AAAAAFF?<mmMaaaaaaaaaaaaaaaaaaaaaaaaabf"))
print(find_longest_substr("1111aa994bbbb1111AAAAAFFcfgBBBBB"))