def nonstop_hotspot(s):
    a,b=map(str.strip,s.split('P'))
    c=0
    for i in a[::-1]:
        if i=='*':
            c+=1
        if i=='#':
            break
    for i in b:
        if i=='*':
            c+=1
        if i=='#':
            break
    return c


print(nonstop_hotspot('*  * #  * P # * #'))