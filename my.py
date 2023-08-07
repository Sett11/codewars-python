import re
def alphabet_war(b):
    a,i=list(b),0
    a.append('0')
    a.insert(0,'0')
    while i<len(a):
        j,t,q=i,'',''
        if a[i]=='[' and i:
            while j:
                j-=1
                if a[j]==']' or a[j]=='0':
                    t=a[j:i]
                    break
            k=i
            while k<len(a):
                k+=1
                if a[k]==']':
                    break
            j=k
            while j<len(a):
                j+=1
                if a[j]=='[' or a[j]=='0':
                    q=a[k+1:j]
                    break
            if (t+q).count('#')>=2:
                a=[h for h in a[:i] if h!='#']+a[k+1:]
        i+=1
    i,f=0,False
    while i<len(a) and '#' in b:
        if a[i] in ['[',']']:
            f=not f
            i+=1
        if not f and i<len(a):
            a[i]='0'
        i+=1
    return re.sub(r'[0\[\]]','',''.join(a))

print(alphabet_war('##abde[fgh]ijk[mn]op'))
print(alphabet_war('#ab#de[fgh]ijk[mn]op'))
print(alphabet_war('#abde[fgh]i#jk[mn]op'))
print(alphabet_war('[a][b][c]'))
print(alphabet_war('#l[j]#[m]pd#w'))
print(alphabet_war('#m[knrz]#[qk]nd#p[i]l#w'))