def f(x):
    x=round(x)
    n=x
    m=x
    while n%5!=0 and m%5!=0:
        n-=1
        m+=1
    return list(filter(lambda e: e%5==0,[m,n]))[0]

def round_to_five(l):
    return list(map(f,list(map(lambda e:e+0.01,l))))

print(round_to_five([22.5, 544.9, 77.5]))