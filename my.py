def domino_reaction(s):
    a,i=list(s),0
    while i<len(a) and a[i]=='|':
        a[i]='/'
        i+=1
    return ''.join(a)

print(domino_reaction("||| ||||//| |/"))
print(domino_reaction("|||||||"))