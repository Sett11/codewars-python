def f(x):
    r=''
    if(x[0]=='^'):r='Take {} step up'.format(x[1])
    if(x[0]=='v'):r='Take {} step down'.format(x[1])
    if(x[0]=='<'):r='Take {} step left'.format(x[1])
    if(x[0]=='>'):r='Take {} step right'.format(x[1])
    if(x[1]>1):r=r.replace('step','steps')
    return r
def walk(c):
    a=[]
    i=0
    j=i+1
    s=c+'a'
    while i<len(s)-1:
        if(s[i]==s[i+1]):
            j=i+1
            while j<len(s):
                if(s[j]!=s[i]):
                    a.append(s[i:j])
                    i=j-1
                    break
                j+=1
        else:
            a.append(s[i])
        i+=1
    a=list(map(lambda e:[e[0],len(e)],a))
    return '\n'.join(list(map(f,a))) if c else 'Paused'

print(walk("<<>"))