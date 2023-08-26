def find_missing(a1,a2):
    a,b=[[i,a1.count(i)] for i in a1],[[i,a2.count(i)] for i in a2]
    for i in a:
        if i[0] not in a2:
            return i[0]
        for j in b:
            if i[0]==j[0] and i[1]!=j[1]:
                return i[0]


print(find_missing([4, 3, 3, 61, 8, 8], [8, 61, 8, 3, 4]))
print(find_missing([1, 2, 3], [1, 3]))
print(find_missing([7], []))