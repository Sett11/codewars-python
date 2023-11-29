from itertools import permutations as p

def best_route(a,b):
    r,o,m=[['Notgnihsaw']+list(i) for i in p(a) if i[-1]=='Notgnihsaw'],{},1e9

    for i in r:
        t=0
        for j in range(len(i)-1):
            t+=b[a.index(i[j])][a.index(i[j+1])]
        m=min(m,t)
        o[t]=i
    
    return o[m][1:]


print(best_route(['Aleppo', 'Shenyang', 'Notgnihsaw', 'Vienna', 'Buenos Aires'], 
                                      [[0, 1800, 1250, 1500, 2450], 
                                       [1400, 0, 1900, 1150, 2000], 
                                       [1300, 1200, 0, 900, 1450],
                                       [3000, 1950, 800, 0, 1700], 
                                       [2800, 2400, 1650, 2250, 0]]))