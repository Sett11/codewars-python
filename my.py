def get_free_urinals(s):
    if '11' in s:
        return -1
    if len(set(s))==1 and s[0]=='0':
        return len([k for k in ['1' if not i&1 else '0' for i,j in enumerate(s)] if k=='1'])
    i,l=(1 if s[0]=='1' else 0),list(s)
    while i<len(l)-1:
        if l[i]=='0' and l[i+1]=='0' and (l[i-1]=='0' or not i):
            l[i]='1'
        i+=1
    if l[-1]=='0' and l[-2]=='0':
        l[-1]='1'
    if l[0]=='0' and l[1]=='0':
        l[0]='1'
    return len([i for i in l if i=='1'])-len([i for i in s if i=='1'])

print(get_free_urinals('10001'))
print(get_free_urinals('00000'))
print(get_free_urinals('01000'))
print(get_free_urinals('0000000000001'))