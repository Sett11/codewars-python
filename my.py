from re import sub

def solve(s):
    s=list(s)
    a=[i for i,j in enumerate(s) if j=='(']
    r=[]
    m=0
    for i in a:
        t=0
        n=i
        while n>=0:
            if s[n]=='(':
                t+=1
            if s[n]==')':
                t-=1
            n-=1
        r.append([i,t])
        m=max(t,m)
    r=[i[0] for i in r if i[1]==m]
    j=0
    while True:
        if s[j]==')':
            break
        j+=1
    if s[r[0]-1].isdigit():
        s[r[0]-1:j+1]=sub(r'[^A-z]','',''.join(s[r[0]-1:j+1]))*int(s[r[0]-1])
    else:
        s[r[0]-1:j+1]=sub(r'[^A-z]','',''.join(s[r[0]-1:j+1]))
    return ''.join(s) if '(' not in s else solve(s)

print(solve("2(a3(b))"))
print(solve("k(a3(b(a2(c))))"))