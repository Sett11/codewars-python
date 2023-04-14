import re
def barbell_weight(b):
    o={'R':25,'B':20,'Y':15,'G':10,'W':5,'r':2.5,'b':2,'y':1.5,'g':1,'w':0.5,'c':2.5}
    return int(sum(list(map(lambda e:o[e], list(re.sub(r'\-','',b[slice(0,10)])))))*2+20)

print(barbell_weight('-------bcr--------------------rcb-------'))