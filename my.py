def beasts(h,t):
    if h/2==t:
        return [h//2,0]
    for i in range(1,t+1):
        if i*5+((t-i)*2)==h:
            return [t-i,i]
    return 'No solutions'

print(beasts(24,12))