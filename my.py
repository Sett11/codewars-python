def team_dinner(a):
    r=sum(a,[])
    s=set(r)
    w=sorted([[r.count(i),i] for i in s],key=lambda e:e[0],reverse=True)
    q=[i[1] for i in w if i[0]==w[0][0]]
    z=[[k[0],len(sum(k[1],[]))] for k in [j for j in [[i,[j for j in a if i in j]] for i in q] if len(j[1])>=len(a)/2]]
    return None if not z else sorted(z,key=lambda e:(e[1],-e[0]),reverse=True)[0][0]


print(team_dinner([[0, 1, 2, 3], [2], [0, 2], [3, 4, 6], [1, 3, 6]]))
print(team_dinner([[0, 1, 2], [1], [1, 2, 4], []]))
print(team_dinner([[0, 1, 5], [2, 3], [4], [], [0, 1]]))
print(team_dinner([[9, 4, 5], []]))