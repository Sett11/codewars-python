def add(s1,s2):
    l=[list(s1),list(s2)]
    a=[]
    for i in l:
        a.append(sum(list(map(lambda e:ord(e),i))))
    return sum(a)

print(add('aa','bb'))