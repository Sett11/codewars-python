def validate(u,p):
    if u=='wow' or p=='wow':
        return False
    r=[]
    v=len(u)<len(p)
    t=len(u) if v else len(p)
    q=u if v else p
    w=p if v else u
    for i in range(t):
        if q[i] in w:
            r.append(1)
        for j in range(i+1,t):
            if q[i:j] in w:
                r.append(len(q[i:j]))
    return max(r)<min(len(u),len(p))/2 if r else True if u and p else False



print(validate("qwertyuiop", "asdfghjkl"))
print(validate("username", "myname"))
print(validate('username', 'e'))