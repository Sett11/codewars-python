from statistics import mean

def f(a,k):
    n,x=len(a),mean(a)
    s=(1/n*sum((i-x)**2 for i in a))**.5*k
    r=[i for i in a if not (i>x+s or i<x-s)]
    return r if r==a else f(r,k)

def clean_mean(a,k):
    return round(mean(f(a,k)),2)

print(clean_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100],3))