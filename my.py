def my_languages(r):
    a=[]
    for i in r:
        if(r[i]>=60):
            a.append([r[i],i])
    return list(map(lambda e:e[1],sorted(a,reverse=True)))

print(my_languages({"Hindi": 60, "Dutch" : 93, "Greek": 71}))