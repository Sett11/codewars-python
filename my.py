def find_caterer(b,p):
    s1,s2,s3=p*15,p*20,p*30-((p*30)//100*20 if p>60 else 0)
    r=[i for i in [[1,s1],[2,s2],[3,s3]] if i[1]<=b]
    return -1 if not p or s1>b else r[0][0] if len(r)==1 else [j[0] for j in r if b-j[1]==min([b-i[1] for i in r])][0]

print(find_caterer(150,10))
print(find_caterer(1500,60))
print(find_caterer(1500,61))