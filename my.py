def f(x,y):
    if(x==y):return 0
    i=1
    while i<5:
        if(y[i:]==x[i:]):return i
        i+=1
    return 5

def joker_card(a,r):
    res=['I type','II type','III type','IV type','V type','Losing card']
    a=''.join(list(map(lambda e:str(e)[-1],a)))
    return list(map(lambda e:res[f(e,a)],r))

print(joker_card([12, 35, 1, 2, 23, 39], ['151239', '251229', '251339']))