def answer(q,l):
    a=[i.split() for i in l]
    q=q.lower().split()
    r=[]
    c=0
    for i in a:
        c=0
        for j in i:
            if(j.lower() in q):
                c+=1
        r.append([i,c])
    r=sorted(r,key=lambda e:e[1],reverse=True)
    r=list(filter(lambda e:e[1]==r[0][1] and e[1],r))
    if(not len(r)):
        return None
    return ' '.join(r[0][0])

print(answer('is beedrill a pokemon', ['python is a programming language', 'RAM stands for Random Access Memory', 'TalonFlame is a pokemon', 'beeedrill OU', 'BeeDrill is a pokemon', 'GNU is not UNIX', 'biology is boring']))