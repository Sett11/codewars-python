def strings_in_max_depth(s):
    r,stack=[],[]
    m=j=0
    for i in s:
        if i=='(':
            j+=1
        if i==')':
            m=max(m,j)
            j-=1
    k=0
    for i,j in enumerate(s):
        if j=='(':
            stack.append(i)
            k+=1
        if j==')':
            if k==m:
                r.append(s[stack.pop()+1:i])
            k-=1
    return r if m else [s]


print(strings_in_max_depth('((AAX(AB)(UP)F(Z))(HH))'))