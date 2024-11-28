def memesorting(s):
    d={'Roma':['b','u','g'],'Maxim':['b','o','o','m'],'Danik':['e','d','i','t','s']}
    for i in s.lower():
        for j in d:
            if i==d[j][0]:
                d[j].pop(0)
                if not d[j]:
                    return j
    return 'Vlad'

print(memesorting('This is programmer meme ecause it has bug'))