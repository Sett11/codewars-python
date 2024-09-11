from collections import Counter

def get_score(a):
    u,c,g=set(a),Counter(a),{1:100,5:50}
    if len(u)==6:
        return 1000
    elif len(u)==2 and len(a)==4 and all(i==2 for i in c.values()):
        return sum(g.get(i,0) for i in a)
    elif len(u)==3 and len(a)==6 and all(i==2 for i in c.values()):
        return 750
    elif len(u)==1 and len(a)==6:
        if 1 in u:
            return 4000
        elif 2 in u:
            return 800
        elif 3 in u:
            return 1200
        elif 4 in u:
            return 1600
        elif 5 in u:
            return 2000
        else:
            return 2400
    elif 5 in c.values():
        x,y=[i for i in c if c[i]==5][0],[i for i in c if c[i]!=5]
        z=sum(g.get(i,0) for i in y)
        if x==1:
            return 3000+z
        elif x==2:
            return 600+z
        elif x==3:
            return 900+z
        elif x==4:
            return 1200+z
        elif x==5:
            return 1500+z
        else:
            return 1800+z
    elif 4 in c.values():
        x,y=[i for i in c if c[i]==4][0],[i for i in c if c[i]!=4]
        z=sum(g.get(i,0) for i in y)
        if x==1:
            return 2000+z
        elif x==2:
            return 400+z
        elif x==3:
            return 600+z
        elif x==4:
            return 800+z
        elif x==5:
            return 1000+z
        else:
            return 1200+z
    x=[i for i in c if c[i]==3]
    if x:
        r=0
        y=[i for i in a if c[i]!=3]
        z=sum(g.get(i,0) for i in y)
        if 1 in x:
            r+=1000
        if 2 in x:
            r+=200
        if 3 in x:
            r+=300
        if 4 in x:
            r+=400
        if 5 in x:
            r+=500
        if 6 in x:
            r+=600
        return r+z
    return sum(g.get(i,0) for i in a)
        
print(get_score([1, 5, 1, 1, 1]))