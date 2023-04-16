def destroyer(s,r=[]):
    a="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    l=list(map(lambda e:list(e),list(s)))
    for i in l:
        r.extend(i)
    while len(r):
        a=a.replace(r.pop(0),'_')
    return a

print(destroyer(({'b', 'b'}, {'C', 'm', 'f'})))