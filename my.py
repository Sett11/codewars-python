def trim(a,i=0):
    while i<len(a):
        if(i!=len(a)-1):
            a[i]=list(map(lambda e:'|' if e=='J' else e,a[i]))
        else:
            a[i]=list(map(lambda e:'...',a[i]))
        i+=1
    return a

print(trim([['...', '|', 'J', '...', 'J'], ['J', 'J', 'J', 'J', '|']]))