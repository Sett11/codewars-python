def lcs(a,b):
    q,s,r=list(b),0,''
    for i in range(len(q)):
        pos=a.find(q[i],s)
        if pos>=s:
            r+=q[i]
            s=pos+1
    return r


print(lcs("anothertest", "notatest"))