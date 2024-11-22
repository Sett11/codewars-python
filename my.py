from re import sub,split

def flesch_kincaid(s):
    a=[[sub(r'[^a-z0-9]','',j) for j in i.strip().split()] for i in split(r'([!.?])+\s',s.lower()) if i[0].isalpha()]
    m1=sum(len(i) for i in a)/len(a)
    b=sum([[sub(r'([aeiou])+','1',j).count('1') for j in i] for i in a],[])
    m2=sum(b)/len(b)
    return round(.39*m1+11.8*m2-15.59,2)

print(flesch_kincaid("A good book is hard to find."))